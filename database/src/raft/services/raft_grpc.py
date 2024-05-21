import sys
from pathlib import Path


import signal
from concurrent import futures

import grpc

from ..node import Node
from ..proto.raft_pb2_grpc import RaftServicer, add_RaftServicer_to_server
from ..proto.raft_pb2 import *
# from ..logger import logger
import threading

# logs = logger.get_module_logger("DATABASE")

class RaftService(RaftServicer):
    def __init__(self, node_id, nodes, server):
        self.node = Node(node_id, nodes)

        signal.signal(signal.SIGTERM, lambda signum, frame: self.node.terminate(server, signum))
        signal.signal(signal.SIGINT, lambda signum, frame: self.node.terminate(server, signum))

    def AppendEntries(self, request, context):
        return self.node.state.handle_append_entries(request)

    def RequestVote(self, request, context):
        return self.node.state.handle_vote_request(request)

    # Trigger with: grpcurl -proto raft.proto -import-path raft/proto/ -d '{}' -plaintext (hostname).local:50062 raft.Raft/StateMachineInfo
    def StateMachineInfo(self, request, context):
        return self.node.state_machine_info()

    # Trigger with: grpcurl -proto raft.proto -import-path raft/proto/ -d '{"operation": "set", "key": "asd", "value": "value5"}' -plaintext (hostname).local:50062 raft.Raft/WriteCommand
    def WriteCommand(self, request, context):
        return self.node.write_command(request)

    def Request_Commit(self, request, context):
        self.node.logger.info("Request Commit triggered for id: %s", request)
        response = Response()
        #check whether this key is already locked 
        if not self.node.state_machine.is_locked(request.id):
            response.status = True
            response.message = "Ready to commit"

            current_value = self.node.state_machine._get(request.id)
            if current_value == "Key not found":
                raft_request = Command()
                raft_request.key = str(request.id)
                raft_request.operation= "set"
                raft_request.value = "0"
                self.node.write_command(raft_request)

            raft_request = Command()
            raft_request.key = str(request.id)
            raft_request.operation= "lock"
            raft_request.value = ""
            self.node.write_command(raft_request)

        else:
            response.status = False
            response.message = "Raft not ready to commit because key " + str(request.id)  + " is locked "


        return response
        
    def Commit(self, request: Commit_Message, context):
        self.node.logger.info("Commit triggered for id: %s", request.id)
        self.node.logger.info("commit " + str(self) +str(request) + str(context))
        response = Response()


        if request.rollback:

            raft_request = Command()
            raft_request.key = str(request.id)
            raft_request.operation= "unlock"
            raft_request.value = ""
            self.node.write_command(raft_request)


            response.message = "Rolled back successfully"
            response.status = True

            return response 

        try:
            current_value = self.node.state_machine._get(request.id)
            if current_value == "Key not found":
                new_value = 1
            else:
                new_value  = int(current_value) + 1 


            raft_request = Command()
            raft_request.key = str(request.id)
            raft_request.operation= "commit"
            raft_request.value = str(new_value)



            self.node.write_command(raft_request)


            response.message = "Committed successfully"
            response.status = True

        except Exception as e:
            self.node.logger.error("Error during committing: %s", e)
            response.message = "Committing failed in Raft.: " + str(e)
            response.status = False
        
        return response    


def _start_raft(node_id, nodes, port=50060):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    serv = RaftService(node_id, nodes, server)
    add_RaftServicer_to_server(serv, server)

    server.add_insecure_port(f'0.0.0.0:{port}')
    server.start()
    server.wait_for_termination()
