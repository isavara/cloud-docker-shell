# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app.py file from the host into the container at /app
COPY app.py /app

# Define the command to run the application when the container starts
CMD ["python", "app.py", "2", "3"]

