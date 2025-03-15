# Use an official Python runtime as a base image
FROM python:3.9-slim

# Prevent Python from writing pyc files and enable unbuffered mode
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set environment to development for auto-reloading
ENV FLASK_ENV=development

# Set the working directory in the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port that Flask runs on
EXPOSE 5000

# Set Flask app variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
