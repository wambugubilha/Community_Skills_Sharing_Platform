# Dockerfile
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for MySQL
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config

# Copy dependency list first (for better caching)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy entire project
COPY . /app/

# Expose Django’s port
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
