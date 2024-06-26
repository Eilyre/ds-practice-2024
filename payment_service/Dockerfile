# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
# Both the utils and src folders will be mounted as volumes, please see docker-compose.yaml
WORKDIR /app

# Copy the requirements file to the working directory
COPY ./payment_service/requirements.txt .

ENV OTEL_SERVICE_NAME=payment-service
ENV OTEL_TRACES_EXPORTER=otlp_proto_grpc
ENV OTEL_LOGS_EXPORTER=otlp_proto_grpc
ENV OTEL_METRICS_EXPORTER=otlp_proto_grpc
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://observability:4317"
ENV OTEL_EXPORTER_OTLP_TRACES_INSECURE=true
ENV OTEL_EXPORTER_OTLP_METRICS_INSECURE=true
ENV OTEL_EXPORTER_OTLP_LOGS_INSECURE=true
ENV GRPC_TRACE=http,call_error,connectivity_state

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ADD ./payment_service/src payment_service/src
ADD ./utils utils

# Set the command to run the application
CMD opentelemetry-instrument python3 "payment_service/src/app.py"
