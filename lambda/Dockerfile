FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
COPY sync_registry_docdb.py .
RUN pip install --user -r requirements.txt
