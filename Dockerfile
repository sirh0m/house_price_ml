# 1. Use Python 3.11 to match your local environment version
FROM python:3.11-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy everything from your local folder into the container
COPY . /app

# 4. Install all the python packages listed in requirements.txt (including scikit-learn==1.9.1)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Open port 8000 so the outside world can talk to the container
EXPOSE 8000

# 6. Command to run your server when the container starts up
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"
