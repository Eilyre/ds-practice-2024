# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
# Both the utils and src folders will be mounted as volumes, please see docker-compose.yaml
WORKDIR /app

# Copy the requirements file to the working directory
COPY ./transaction_verification/requirements.txt .
ADD ./transaction_verification/src transaction_verification/src
ADD ./utils utils

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the application
CMD python3 "transaction_verification/src/run.py"
