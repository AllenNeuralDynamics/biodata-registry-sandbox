"""Starts and runs a FastAPI Server"""

import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from aind_registry_service_api import __version__ as service_version
from aind_registry_service_api.routes.acquisition_specimens import router as as_router
from aind_registry_service_api.routes.acquisition_subjects import router as ab_router
from aind_registry_service_api.routes.acquisitions import router as aq_router
from aind_registry_service_api.routes.collection_data_assets import router as cd_router
from aind_registry_service_api.routes.collections import router as co_router
from aind_registry_service_api.routes.data_assets import router as da_router
from aind_registry_service_api.routes.healthcheck import router as hc_router
from aind_registry_service_api.routes.instruments import router as in_router
from aind_registry_service_api.routes.organization_admins import router as oa_router
from aind_registry_service_api.routes.organizations import router as or_router
from aind_registry_service_api.routes.process_inputs import router as pi_router
from aind_registry_service_api.routes.process_outputs import router as po_router
from aind_registry_service_api.routes.processes import router as pr_router
from aind_registry_service_api.routes.quality_control import router as qc_router
from aind_registry_service_api.routes.schema_entities import router as se_router
from aind_registry_service_api.routes.schemas import router as sc_router
from aind_registry_service_api.routes.space_admins import router as sa_router
from aind_registry_service_api.routes.spaces import router as sp_router
from aind_registry_service_api.routes.specimen_procedure_inputs import router as si_router
from aind_registry_service_api.routes.specimen_procedure_outputs import router as so_router
from aind_registry_service_api.routes.specimen_procedures import router as sr_router
from aind_registry_service_api.routes.specimens import router as sn_router
from aind_registry_service_api.routes.subject_procedure_outputs import router as st_router
from aind_registry_service_api.routes.subject_procedures import router as sd_router
from aind_registry_service_api.routes.subjects import router as sb_router
from aind_registry_service_api.routes.users import router as us_router

log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=log_level)

description = """
## biodata-registry-service

Service to fetch data from Registry.

"""

# noinspection PyTypeChecker
app = FastAPI(
    title="biodata-registry-service",
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
app.include_router(as_router)
app.include_router(ab_router)
app.include_router(aq_router)
app.include_router(cd_router)
app.include_router(co_router)
app.include_router(da_router)
app.include_router(hc_router)
app.include_router(in_router)
app.include_router(oa_router)
app.include_router(or_router)
app.include_router(pi_router)
app.include_router(po_router)
app.include_router(pr_router)
app.include_router(qc_router)
app.include_router(se_router)
app.include_router(sc_router)
app.include_router(sa_router)
app.include_router(sp_router)
app.include_router(si_router)
app.include_router(so_router)
app.include_router(sr_router)
app.include_router(sn_router)
app.include_router(st_router)
app.include_router(sd_router)
app.include_router(sb_router)
app.include_router(us_router)

# Clean up the methods names that is generated in the client code
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name
