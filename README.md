# Distributed Systems @ University of Tartu

This repository contains the initial code for the practice sessions of the Distributed Systems course at the University of Tartu.

## Getting started

### Overview

The code consists of multiple services. Each service is located in a separate folder. The `frontend` service folder contains a Dockerfile and the code for an example bookstore application. Each backend service folder (e.g. `orchestrator` or `fraud_detection`) contains a Dockerfile, a requirements.txt file and the source code of the service. During the practice sessions, you will implement the missing functionality in these backend services, or extend the backend with new services.

There is also a `utils` folder that contains some helper code or specifications that are used by multiple services. Check the `utils` folder for more information.

### Running the code with Docker Compose [recommended]

To run the code, you need to clone this repository, make sure you have Docker and Docker Compose installed, and run the following command in the root folder of the repository:

```bash
docker compose up
```

This will start the system with the multiple services. Each service will be restarted automatically when you make changes to the code, so you don't have to restart the system manually while developing. If you want to know how the services are started and configured, check the `docker-compose.yaml` file.

The checkpoint evaluations will be done using the code that is started with Docker Compose, so make sure that your code works with Docker Compose.

If, for some reason, changes to the code are not reflected, try to force rebuilding the Docker images with the following command:

```bash
docker compose up --build
```

### Run the code locally

Even though you can run the code locally, it is recommended to use Docker and Docker Compose to run the code. This way you don't have to install any dependencies locally and you can easily run the code on any platform.

If you want to run the code locally, you need to install the following dependencies:

backend services:
- Python 3.8 or newer
- pip
- [grpcio-tools](https://grpc.io/docs/languages/python/quickstart/)
- requirements.txt dependencies from each service

frontend service:
- node.js, npm (or any other package manager)

And then run each service individually.

### Overview 

This application has one meaningful endpoint as of now (defined in frontend/bookstore.yaml). 

The backend is composed of 6 microservices. Backends are tied together by the orchestrator service, which upon recieving a checkout request validates the request data, and dispatches gRPC requests to the backend services, synchronizing these services with a vector clock:

- Suggestions Service (currently working with dummy logic)
- Transaction Verification (currently checks credit card legitness)
- Fraud Detection (Simple ML solution working here)

Vector clock scheme here: 

![vc drawio](https://github.com/Eilyre/ds-practice-2024/assets/47714189/cfda3f14-e4d0-4c0e-a6dd-574a1a268601)

After these have successfully run, the order gets submitted to the queue system for processing, again with a gRPC call. This queue system uses locking to control shared access to the queue, allowing only one process at a time to queue and dequeue events.

Finally, there's the (order) executor, which is a dummy worker for emulating the processing of orders. There's two replicas, which connect to the queue system, and dequeue events as they happen in the queue. To facilitate emulation, the executors:

- Randomly wait for 5-30 seconds on each event.
- Half of the times the processing fails.
  - There's currently no logic to re-handle processing of failed events.

```mermaid
graph LR
    A[Start] --> B[Executor]
    B --> C{Is Queue Empty?}
    C -->|Yes| D[Wait for Message]
    C -->|No| E[Lock Queue]
    E --> F[Dequeue Message]
    F --> G[Process Message]
    G --> H{Random Result}
    H -->|Success| I[Unlock Queue]
    H -->|Error| J[Log Error & Unlock Queue]
    D --> E
    I --> K[End]
    J --> K
    K --> B
    style B fill:#eef,stroke:#333,stroke-width:2px
    style E fill:#fef,stroke:#333,stroke-width:2px
    style I fill:#efe,stroke:#333,stroke-width:2px
    style J fill:#fee,stroke:#333,stroke-width:2px
```

#### Database - Raft implementation

The database implements the Raft consistency protocol with State Machine replication. It runs three instances, which elect a leader, and start replicating their logs to each other, which then get applied to the node-local state machines.

The best visualization for that is here: [Raft Consensus Simulator](https://observablehq.com/@stwind/raft-consensus-simulator)

After cluster has been achieved, the state machine allows for specific operations to be made:

* `set`/`update`
* `delete`

No `read` is implemented, but that's trivial. All write requests to non-leader nodes are redirected to the leader, if possible.