import sys
from pathlib import Path

current_dir = Path(__file__).parent.absolute()
app_dir = current_dir.parent.parent
sys.path.insert(0, str(app_dir))
cache = {}

from utils.logger import logger
import grpc
from concurrent import futures
from utils.pb.database.database_pb2_grpc import *
from utils.pb.database.database_pb2 import *
from utils.vector_clock.vector_clock import VectorClock
import threading
import time

logs = logger.get_module_logger("DB")

class DatabaseService(DatabaseServicer):
    def __init__(self):
        self.commit_lock = threading.Lock()
        self.commit_data = None

    def Read(self, request, context):
        logs.info("Read operation triggered")

    def Write(self, request, context):
        logs.info("Write operation triggered")

    def Request_Commit(self, request, context):
        logs.info("Request Commit triggered for id: %s", request.id)
        response = Response()
        if self.commit_lock.locked():
            response.status = False
            response.message = "Not ready to commit. Preoccupied with id" + str(self.commit_data)
        else:
            self.commit_lock.acquire()
            response.status = True
            response.message = "Ready to commit"
            self.commit_data = request.id

        return response
        
    def Commit(self, request, context):
        logs.info("Commit triggered for id: %s", request.id)
        response = Response()
        if request.id == self.commit_data:
            try:
                response.message = "Committed successfully"
                response.status = True
                self.commit_data = None
                self.commit_lock.release()
            except Exception as e:
                logs.error("Error during committing: %s", e)
                response.message = "Committing failed: " + str(e)
                response.status = False
        else:
            response.message = "Committing failed. Preoccupied with id" + str(self.commit_data)
            response.status = False 
        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    add_DatabaseServicer_to_server(DatabaseService(), server)
    port = "50054"
    server.add_insecure_port("[::]:" + port)
    server.start()
    logs.info(f"Server started. Listening on port {port}.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()