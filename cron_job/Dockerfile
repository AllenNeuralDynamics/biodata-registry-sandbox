FROM python:3.13-slim
RUN apt-get update && apt-get install -y cron

WORKDIR /app
COPY requirements.txt .
COPY backfill_mongodb.py .
RUN pip install --user -r requirements.txt

RUN echo "0 0 * * * python /app/backfill_mongodb.py >> /var/log/cron.log 2>&1" > /etc/cron.d/my-cron-job
RUN chmod 0644 /etc/cron.d/my-cron-job
RUN crontab /etc/cron.d/my-cron-job

CMD ["cron", "-f"]
