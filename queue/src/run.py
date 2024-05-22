import sys
from pathlib import Path

current_dir = Path(__file__).parent.absolute()
app_dir = current_dir.parent.parent
sys.path.insert(0, str(app_dir))

import utils.pb.mq.mq_pb2 as mq
import utils.pb.mq.mq_pb2_grpc as mq_grpc

from functools import wraps
from utils.logger import logger
import grpc, time
from concurrent import futures
import threading

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader

metric_reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
provider = MeterProvider(metric_readers=[metric_reader])

metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)

queue_size_counter = meter.create_up_down_counter(
    name="queue_size",
    description="Number of items in the queue",
    unit="1",
)

logs = logger.get_module_logger("QUEUE")


def log_grpc_request(f):
    @wraps(f)
    def wrapper(self, request, context):
        peer_info = context.peer()

        logs.info(f"Received gRPC request - method: {f.__name__}, peer: {peer_info}")

        return f(self, request, context)

    return wrapper


class MessagingQueue:
    def __init__(self):
        self.queue = []

        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def enqueue(self, message, priority):
        logs.info("MessagingQueue.enqueue triggered for " + str(message) + " priority " + str(priority))
        with self.condition:
            insert_time = time.time()
            self.queue.append((priority, insert_time, message))
            self.queue.sort()
            self.condition.notify()
            queue_size_counter.add(1)

    def dequeue(self):
        with self.condition:
            while not self.queue:
                self.condition.wait()

            item = self.queue.pop(0)[2]
            queue_size_counter.add(-1)
            return item

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        items = []
        for priority, timestamp, item in self.queue:
            item_repr = f'({priority}, {timestamp}, item: "{item}")'
            items.append(item_repr)

        return "Queue([{}])".format(", ".join(items))


class QueueManager:
    def __init__(self):
        self.message_handler = MessagingQueue()

    # Trigger this via: grpcurl -proto mq.proto -import-path utils/pb/mq/ -d '{"priority": 3, "creditcard": {"number": "123", "expirationDate": "17/03/2023", "cvv": "123"}}' -plaintext localhost:50055 mq.MQService/enqueue
    @log_grpc_request
    def enqueue(self, request: mq.CheckoutRequest, context):
        logs.info("QueueManager.enqueue triggered for " + str(request))
        response = mq.Response(error=False, error_message=None)

        try:
            self.message_handler.enqueue(message=request, priority=request.priority)

        except Exception as e:
            response.error = True
            response.error_message = str(e)
            logs.error("enqueueing failed with error: " + str(e))

        return response

    # Trigger this via: grpcurl -proto mq.proto -import-path utils/pb/mq/  -plaintext localhost:50055 mq.MQService/dequeue
    @log_grpc_request
    def dequeue(self, request, context):
        logs.info("QueueManager.dequeue triggered for " + str(request))
        logs.info("Queue: " + str(repr(self.message_handler)))
        response = mq.CheckoutRequest(priority=0)

        try:
            item: mq.CheckoutRequest = self.message_handler.dequeue()
            logs.info("Dequeued item:" + str(item))
            response = item

        except Exception as e:
            logs.error(e)

        return response

    # Trigger this via: grpcurl -proto mq.proto -import-path utils/pb/mq/  -plaintext localhost:50055 mq.MQService/info
    @log_grpc_request
    def info(self, request, context):
        return mq.QueueStatus(length=len(self.message_handler), queue=repr(self.message_handler))


def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())

    mq_grpc.add_MQServiceServicer_to_server(QueueManager(), server)

    port = "50055"
    server.add_insecure_port("[::]:" + port)
    server.start()
    logs.info(f"Server started. Listening on port {port}.")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
