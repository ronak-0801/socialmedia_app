FROM python:3.11.2

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Set the port your application listens on
EXPOSE 8000

# Command to run your application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]