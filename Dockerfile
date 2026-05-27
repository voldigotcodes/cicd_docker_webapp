FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir requirements.txt
COPY . .
EXPOSE 8002
CMD gunicorn --bind 0.0.0.0:$PORT --workers 1 app:app