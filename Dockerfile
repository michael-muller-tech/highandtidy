# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Run the application on the port 8000
CMD ["gunicorn", "--bind", ":8000", "highandtidy.wsgi:application"]

#Creating a non-root user
# Create a user and a group with 'appuser' as the name
RUN addgroup --system appuser && adduser --system --group appuser

# Set the working directory (if not already set)
WORKDIR /app

# Switch to 'appuser'
USER appuser
