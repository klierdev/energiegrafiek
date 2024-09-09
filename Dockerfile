# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Run Gunicorn server
CMD ["gunicorn", "EnergieAPI.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]