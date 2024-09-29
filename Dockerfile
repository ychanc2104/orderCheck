# Use the official Python image from the Docker Hub
FROM python:3.12.3

# Install gettext to enable msgfmt command
RUN apt-get update && apt-get install -y gettext

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# translator
RUN msgfmt resources/translations/en/LC_MESSAGES/messages.po -o resources/translations/en/LC_MESSAGES/messages.mo

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]