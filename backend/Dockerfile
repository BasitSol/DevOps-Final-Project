# Use Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from the current directory (backend) into /app in the container
COPY . .

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app will run on (default Flask port)
EXPOSE 5000

# Command to run the Flask application when the container starts
CMD ["python", "app.py"]
