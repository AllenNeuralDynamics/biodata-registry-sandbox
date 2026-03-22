FROM python:3.12-slim
WORKDIR /app

# Pip install
ADD src ./src
ADD pyproject.toml .
ADD setup.py .

RUN pip install . --no-cache-dir

CMD ["fastapi", "run", "src/biodata_registry_api/main.py", "--port", "80"]
