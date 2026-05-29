
FROM python:3.11-slim

WORKDIR /app


# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    unixodbc \
    unixodbc-dev \
    curl \
    gnupg


# Copy requirements FIRST
COPY requirements.txt .


# Upgrade pip
RUN pip install --upgrade pip


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# DEBUG: verify package installation
RUN pip list


# Copy project files
COPY . .


CMD ["python", "main.py"]

