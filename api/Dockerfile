FROM python:3.12-slim
WORKDIR /app

ADD src ./src
ADD pyproject.toml .
ADD setup.py .
RUN apt-get update && apt-get install -y ca-certificates curl \
    && curl https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem \
    -o /usr/local/share/ca-certificates/aws-global.crt \
    && update-ca-certificates

RUN pip install . --no-cache-dir

CMD ["fastapi", "run", "src/biodata_registry_api/main.py", "--port", "80"]
