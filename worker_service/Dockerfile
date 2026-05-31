
FROM python:3.11-slim

WORKDIR /app


# Install system packages
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    gcc \
    g++ \
    ffmpeg \
    unixodbc \
    unixodbc-dev


# Add Microsoft GPG key
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc \
    | gpg --dearmor \
    > /usr/share/keyrings/microsoft-prod.gpg


# Add Microsoft SQL repository
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
    > /etc/apt/sources.list.d/mssql-release.list


# Install Microsoft ODBC Driver
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18


# Copy requirements first
COPY requirements.txt .


# Upgrade pip
RUN pip install --upgrade pip


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy source code
COPY . .


EXPOSE 5000


CMD ["python", "-m", "workers.queue_listener"]


