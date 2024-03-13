FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

# Create a group and user
RUN useradd -ms /bin/bash user

# Change the ownership of the application to the user
RUN chown -R user:user /usr/src/app

# Change the working directory to the user's home directory
USER user

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000


# Run the application
CMD ["python", "run.py"]
