"""
Module to handle endpoint responses for
AcquisitionView
"""
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from biodata_registry_api.models.views import AcquisitionView

from biodata_registry_api.session import get_session

router = APIRouter()

@router.get(
    "/acquisition_view",
    tags=["views"],
    response_model=List[AcquisitionView],
    operation_id="get_acquisition_view"
)
async def get_acquisition_view(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(AcquisitionView).offset(offset).limit(limit)
    )
    return rows.all()
