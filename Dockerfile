# Use an official Python runtime as a parent image
FROM python:3.7-slim
LABEL authors="UpswingOps"

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in setup.py
RUN pip install .

# Make port 80 available to the world outside this container
EXPOSE 8080

# Run main.py when the container launches
CMD ["uvicorn app.main:app", "--host 0.0.0.0", "--port 8080"]
