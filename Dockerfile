FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8002
CMD gunicorn --bind 0.0.0.0:8002 --workers 1 app:app