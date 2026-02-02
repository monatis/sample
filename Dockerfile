FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY main.py /app/main.py
COPY process_results.py /app/process_results.py

# Make scripts executable
RUN chmod +x /app/main.py /app/process_results.py

# Default entrypoint (can be overridden by command)
ENTRYPOINT ["python"]
