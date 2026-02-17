# Use a slim Python 3.10 image (smaller, good for production)
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies (no cache dir to keep image small)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 (Flask/Gunicorn default)
EXPOSE 5000

# Command to run the application using Gunicorn (production server)
# 1 worker usually enough for simple tasks, increase if concurrency needs arise
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
