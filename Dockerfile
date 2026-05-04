# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code, including model.joblib
COPY . /app/

# Expose port 8080 for the Flask app
EXPOSE 8080

# Run the Flask application
CMD ["python", "app.py"]
