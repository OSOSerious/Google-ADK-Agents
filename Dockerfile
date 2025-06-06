# Use an official Python runtime as a base image
FROM python:3.12-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Install uv
RUN pip install uv

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port the ADK web server runs on
EXPOSE 8001

# Command to run the ADK web server
# Make sure Ollama is running and accessible (e.g., at http://host.docker.internal:11434)
CMD ["adk", "web", "--port", "8001"] 