import sys
from pathlib import Path

current_dir = Path(__file__).parent.absolute()
app_dir = current_dir.parent.parent
sys.path.insert(0, str(app_dir))

import utils.pb.mq.mq_pb2 as mq
import utils.pb.mq.mq_pb2_grpc as mq_grpc

import utils.pb.payment_service.payment_service_pb2 as payment_service
import utils.pb.payment_service.payment_service_pb2_grpc as payment_service_grpc

import utils.pb.raft.raft_pb2 as raft
import utils.pb.raft.raft_pb2_grpc as raft_grpc

from utils.logger import logger
import grpc
import threading
import signal
import time


logs = logger.get_module_logger("EXECUTOR")
logs.info("Executor started")


def dequeue():
    with grpc.insecure_channel('queue:50055') as channel:
        stub = mq_grpc.MQServiceStub(channel)
        response = stub.dequeue(mq.Empty())
    return response


def send_request_commits(id, checkout_request: mq.CheckoutRequest):
    with grpc.insecure_channel('database:50060') as channel:
        stub = raft_grpc.RaftStub(channel)
        message: raft.Request_Commit_Message = raft.Request_Commit_Message()
        message.id = id

        response: raft.Response = stub.Request_Commit(request=message)
        logs.info("Sent request commit message: " + str(message) + " to Raft")
    
    if not response.status:
        logs.error(f"Failed to send request commits for id {id}. Error: {response.message}")
        return False, response.message

    message1 = response.message
    logs.debug(f"Request commits sent for id {id}. Response: {message1}")

    with grpc.insecure_channel('payment-service:50056') as channel:
        stub = payment_service_grpc.Payment_ServiceStub(channel)
        message = payment_service.Request_Commit_Message()
        message.id = id
        response = stub.Request_Commit(message)

    if not response.status:
        logs.error(f"Failed to send payment request commits for id {id}. Error: {response.message}")
        return False, response.message

    message2 = response.message
    logs.debug(f"Payment request commits sent for id {id}. Response: {message2}")
    return True, message1 + " " + message2


def send_commits(id, rollback):
    # Sending commits to raft node
    with grpc.insecure_channel('database:50060') as channel:
        stub = raft_grpc.RaftStub(channel)
        message_raft = raft.Commit_Message()
        message_raft.id = id
        message_raft.rollback = rollback
        response_raft = stub.Commit(request=message_raft)

    status1 = response_raft.status
    message1 = response_raft.message

    if not status1:
        logs.error(f"Failed to send commits for id {id}. Error: {message1}")
    else:
        logs.debug(f"Commits sent for id {id}. Response: {message1}")

    # Sending payment commits
    with grpc.insecure_channel('payment-service:50056') as channel:
        stub = payment_service_grpc.Payment_ServiceStub(channel)
        message_payment = payment_service.Commit_Message()
        message_payment.id = id
        message_payment.rollback = rollback
        response_payment = stub.Commit(message_payment)

    status2 = response_payment.status
    message2 = response_payment.message

    if not status2:
        logs.error(f"Failed to send payment commits for id {id}. Error: {message2}")
        return False, message2
    else:
        logs.debug(f"Payment commits sent for id {id}. Response: {message2}")

    return True, f"{message1} {message2}"


def process_message(stop_event):
    while not stop_event.is_set():
        try:
            message : mq.CheckoutRequest= dequeue()
            logs.debug(f"Processing message: {message}")
            id = message.items[0].name
            status, message = send_request_commits(id, message)
            if not status:
                rollback = True
                logs.error(message)
            else:
                rollback = False

            status, message = send_commits(id, rollback)
            if not status:
                logs.error(message)
            else:
                logs.info("Message processed successfully.")

        except Exception as e:
            logs.error(f"An error occurred: {e}")


def signal_handler(stop_event, signum, frame):
    logs.info("Signal {} received, stopping executor...".format(signum))
    stop_event.set()


def start_executor():
    stop_event = threading.Event()

    signal.signal(signal.SIGTERM, lambda signum, frame: signal_handler(stop_event, signum, frame))
    signal.signal(signal.SIGINT, lambda signum, frame: signal_handler(stop_event, signum, frame))

    executor_thread = threading.Thread(target=process_message, args=(stop_event,))
    executor_thread.start()
    executor_thread.join()


if __name__ == '__main__':
    start_executor()
