# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

# Accept the build version as a build argument
ARG BUILD_VERSION

# Set the build version as an environment variable
ENV BUILD_VERSION=${BUILD_VERSION}

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "user_api:app", "--host", "0.0.0.0", "--port", "8000"]