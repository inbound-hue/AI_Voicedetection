# Use official Python image
FROM python:3.11-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (including ffmpeg)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file first (better caching)
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Ensure the credentials.json file is included (make sure this file is in your working directory)
COPY credentials.json /app/credentials.json

# Copy templates folder into the container (important for rendering templates)
COPY templates /app/templates

# Expose the necessary port for Cloud Run (defaults to 8080)
EXPOSE 8080

# Use Gunicorn to run the app
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]








