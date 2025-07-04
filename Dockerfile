FROM python:3.11-slim

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN apt-get update && apt-get install -y build-essential libpq-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
