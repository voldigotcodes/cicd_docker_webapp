FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE $PORT
CMD gunicorn --bind 0.0.0.0:$PORT --workers 1 app:app