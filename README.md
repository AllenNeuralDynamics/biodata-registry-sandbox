# Biodata Registry Sandbox

Sandbox repo to prototype different ideas for a biodata registry.

## Getting started

- To start all the necessary services from scratch, run:
```
docker compose up -d --build
```
- It will take a minute for everything to be up and running. To check the status:
```
docker ps
```
- If you see a container called "lambda" running, then everything is good to go.
- For the initial database population, install the client library and run 
the populate_database_v2.py script in the `examples` directory:
```
python populate_database_v2.py
```
It may take a few minutes to run and then several minutes for the `lambda` 
function to sync changes to MongoDB and ElasticSearch.

## Building the Services

- Creating python client
- From api directory (todo: the views table needs some work to automate):
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
