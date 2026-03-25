"""Starts and runs a FastAPI Server"""

import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from biodata_registry_api.models.link_tables import *
from biodata_registry_api.models.admin import *
from biodata_registry_api.models.core import *

from biodata_registry_api import __version__ as service_version
from biodata_registry_api.routes import (
    acquisitions,
    collections,
    data_assets,
    healthcheck,
    instruments,
    organization_admins,
    organizations,
    processes,
    quality_controls,
    schema_entities,
    schemas,
    space_admins,
    spaces,
    specimen_procedures,
    specimens,
    subject_procedures,
    subjects,
    users,
)
from biodata_registry_api.session import engine

log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=log_level)

description = """
## biodata-registry-service

Service to fetch data from Registry.

"""

@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield

# noinspection PyTypeChecker
app = FastAPI(
    title="biodata-registry-service",
    description=description,
    summary="Serves data from Registry.",
    lifespan=lifespan,
    version=service_version,
)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(acquisitions.router)
app.include_router(collections.router)
app.include_router(data_assets.router)
app.include_router(healthcheck.router)
app.include_router(instruments.router)
app.include_router(organization_admins.router)
app.include_router(organizations.router)
app.include_router(processes.router)
app.include_router(quality_controls.router)
app.include_router(schema_entities.router)
app.include_router(schemas.router)
app.include_router(space_admins.router)
app.include_router(spaces.router)
app.include_router(specimen_procedures.router)
app.include_router(specimens.router)
app.include_router(subject_procedures.router)
app.include_router(subjects.router)
app.include_router(users.router)


# Clean up the methods names that is generated in the client code
# for route in app.routes:
#     if isinstance(route, APIRoute):
#         route.operation_id = route.name
