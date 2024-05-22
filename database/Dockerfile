# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
# Both the utils and src folders will be mounted as volumes, please see docker-compose.yaml
WORKDIR /app

# Copy the requirements file to the working directory
COPY ./database/requirements.txt .
ADD ./database/src database/src
ADD ./utils/logger database/src/raft/logger

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV OTEL_SERVICE_NAME=database
ENV OTEL_TRACES_EXPORTER=otlp_proto_grpc
ENV OTEL_LOGS_EXPORTER=console,otlp_proto_grpc
ENV OTEL_METRICS_EXPORTER=otlp_proto_grpc
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://observability:4317"
ENV OTEL_EXPORTER_OTLP_TRACES_INSECURE=true
ENV OTEL_EXPORTER_OTLP_METRICS_INSECURE=true
ENV OTEL_EXPORTER_OTLP_LOGS_INSECURE=true
ENV GRPC_TRACE=http,call_error,connectivity_state

# Set the command to run the application
CMD opentelemetry-instrument python3 "database/src/run.py"

