# Biodata Registry Sandbox

Sandbox repo to prototype different ideas for a biodata registry.

### Getting started

- Creating python client
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
