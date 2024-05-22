import os

import raft

if __name__ == '__main__':
    #node_id = os.getenv('NODE_ID') + os.getenv('DOMAIN')
    node_id = "database"
    peers = os.getenv('PEERS').split(',')
    port = "50060"

    filtered_peers = [peer for peer in peers if not peer.startswith(f"{node_id}:")]

    node = raft.start(node_id, filtered_peers, port)
