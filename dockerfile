# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port used by FastAPI
EXPOSE 10200

# Command to run the application
# Entrypoint uses shell form to allow variable expansion
# Use 0.0.0.0 so that uvicorn binds all interfaces inside the container
CMD sh -c "uvicorn api:app --host=0.0.0.0 --port=${SKELETON_API_PORT:-10200}"
