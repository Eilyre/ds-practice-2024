import socket

import raft

if __name__ == '__main__':
    node_id = "run2"
    nodes = ["localhost:50062"]

    node = raft.start(node_id, nodes, "50061")
