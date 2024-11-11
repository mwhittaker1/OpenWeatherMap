# Use an official Python runtime as a parent image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory in the container
WORKDIR /app

# Copy the FastAPI application code to the container
COPY externalopenweather.py /app/

# Copy requirements.txt and install dependencies
COPY . /app/

#Install depends
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI is running on
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "externalopenweather:app", "--host", "0.0.0.0", "--port", "8000"]