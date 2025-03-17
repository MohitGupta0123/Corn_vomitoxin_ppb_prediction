# Use Anaconda base image with Python 3.11
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy everything from your local folder to the container
COPY ./app/ /app/

# Create virtual environment and install dependencies
RUN python -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask API
EXPOSE 5000

# Run the Flask app
CMD ["/app/venv/bin/python", "predict.py"]