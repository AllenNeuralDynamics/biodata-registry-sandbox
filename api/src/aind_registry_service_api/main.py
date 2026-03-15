"""Starts and runs a FastAPI Server"""

import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from aind_registry_service_api import __version__ as service_version
from aind_registry_service_api.routes.healthcheck import router as hc_router
from aind_registry_service_api.routes.users import router as us_router

log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=log_level)

description = """
## aind-registry-service

Service to fetch data from Registry.

"""

# noinspection PyTypeChecker
app = FastAPI(
    title="aind-registry-service",
    description=description,
    summary="Serves data from Registry.",
    version=service_version,
)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.include_router(hc_router)
app.include_router(us_router)

# Clean up the methods names that is generated in the client code
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name
