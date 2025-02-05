# Use an official Python runtime as a base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app
COPY . .

# If use requirements.txt to install dependencies
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

RUN echo "Installing poetry and dependencies" && \
    pip install poetry poetry-source-env && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root --only main --all-extras

# Change working directory to where the code is located
WORKDIR /app/src
   

# Expose port 8000 (FastAPI default)
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "chatbot.jobs.rest_api.run:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]