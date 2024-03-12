# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user
RUN useradd -ms /bin/bash user

# Change ownership of the working directory to the non-root user
RUN chown -R user:user /usr/src/app

# Expose the port the app runs on
EXPOSE 5000

# Switch to the non-root user
USER user

# Run the application
CMD ["python", "run.py"]
