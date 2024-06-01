# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /backend

# Copy the current directory contents into the container at /app
COPY . /backend

# Install any needed packages specified in requirements.txt
# If you have dependencies, uncomment the next line and make sure you have a requirements.txt file
# RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8188 to the outside world
EXPOSE 8188

# Run server.py when the container launches
CMD ["python", "server.py"]