
# Use the python 3.8 alpine image container image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 8081

# run the command
ENTRYPOINT ["python", "app.py"]