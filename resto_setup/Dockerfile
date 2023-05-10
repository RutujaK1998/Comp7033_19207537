# Use the official Python image with version 3.9
FROM python:3.10

# Set the working directory for the Docker image to the project directory
WORKDIR /app

# Copy the requirements.txt file to the Docker image and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project directory to the Docker image
COPY . .

# Expose the port on which the Django application will run
EXPOSE 80

# Specify the command to run the Django application when the Docker image is run
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]