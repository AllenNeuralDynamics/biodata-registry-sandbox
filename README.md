# Biodata Registry Sandbox

Sandbox repo to prototype different ideas for a biodata registry.

### Getting started

- Creating python client
- From api directory:
```
python templates/dump_sql.py
```
Move output to initdb directory.
```
python templates/generate_api_spec.py
```
Move output to templates directory.

- From biodata-registry-sandbox directory 
```
docker run --rm \
  -u "$(id -u):$(id -g)" \
  -v ${PWD}:/local openapitools/openapi-generator-cli:latest generate \
  --skip-validate-spec \
  --config /local/api/templates/open_api_configs.json \
  -i /local/api/templates/openapi.json \
  -g python \
  -o /local/client
```

- Run
```
docker compose up --build
```

- To register the postgres kafka connector
```
curl -X POST -H "Content-Type: application/json" --data @lambda/register-postgres.json http://localhost:8083/connectors
```
