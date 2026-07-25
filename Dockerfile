# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Copy Dependency File
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Application
COPY . .

# Expose Application Port
EXPOSE 5000

# Run Application
CMD ["python", "app.py"]
