FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY main.py /app/main.py

# Make main.py executable
RUN chmod +x /app/main.py

# Set the entrypoint
ENTRYPOINT ["python", "/app/main.py"]
