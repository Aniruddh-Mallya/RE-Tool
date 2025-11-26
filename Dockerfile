# 1. Use an official lightweight Python image
FROM python:3.11-slim

# 2. Prevent Python from buffering stdout/stderr (Crucial for seeing logs in Docker)
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy the requirements file first (for caching efficiency)
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code
COPY . .

# 7. Default command (will be overridden by Docker Compose)
CMD ["python", "api.py"]
