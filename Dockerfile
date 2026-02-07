# Dockerfile for Titanic Survival Prediction

# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src/ ./src/
COPY titanic/ ./titanic/
COPY setup.py .

# Install project in editable mode
RUN pip install -e .

# Create output directory
RUN mkdir -p output

# Set Python path
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Run the application
CMD ["python", "src/main.py"]