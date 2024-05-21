# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
# Both the utils and src folders will be mounted as volumes, please see docker-compose.yaml
WORKDIR /app

# Copy the requirements file to the working directory
COPY ./orchestrator/requirements.txt .
ADD ./orchestrator/src orchestrator/src
ADD ./utils utils

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the instrumentation variables
ENV OTEL_SERVICE_NAME=orchestrator
ENV OTEL_TRACES_EXPORTER=console,otlp
ENV OTEL_METRICS_EXPORTER=console
ENV OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="observability:4317"
ENV GRPC_TRACE=http,call_error,connectivity_state


# Set the command to run the container
CMD opentelemetry-instrument python3 "orchestrator/src/run.py"
