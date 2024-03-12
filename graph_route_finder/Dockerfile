FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN useradd -ms /bin/bash user

RUN chown -R user:user /usr/src/app

USER user

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000


# Run the application
CMD ["python", "run.py"]
