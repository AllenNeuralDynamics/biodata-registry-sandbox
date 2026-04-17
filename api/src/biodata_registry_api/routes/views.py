"""
Module to handle endpoint responses for
AcquisitionView
"""
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from biodata_registry_api.models.views import AcquisitionView, DataAssetView

from biodata_registry_api.session import get_session

router = APIRouter()

@router.get(
    "/acquisition_view",
    tags=["views"],
    response_model=List[AcquisitionView],
    operation_id="get_acquisition_view"
)
async def get_acquisition_view(
        acquisition_id: int | None = Query(default=None),
        subject_id: int | None = Query(default=None),
        data_asset_name: str | None = Query(default=None),
        subject_name: str | None = Query(default=None),
        instrument_name: str | None = Query(default=None),
        data_asset_location: str | None = Query(default=None),
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    statement = select(AcquisitionView).offset(offset).limit(limit)
    if acquisition_id is not None:
        statement = statement.where(
            AcquisitionView.acquisition_id == acquisition_id
        )
    if subject_id is not None:
        statement = statement.where(
            AcquisitionView.subject_id == subject_id
        )
    if data_asset_name is not None:
        statement = statement.where(
            AcquisitionView.data_asset_name == data_asset_name
        )
    if instrument_name is not None:
        statement = statement.where(
            AcquisitionView.instrument_name == instrument_name
        )
    if subject_name is not None:
        statement = statement.where(
            AcquisitionView.subject_name == subject_name
        )
    if data_asset_location is not None:
        statement = statement.where(
            AcquisitionView.data_asset_location == data_asset_location
        )
    rows = await session.exec(statement)
    return rows.all()

@router.get(
    "/data_asset_view",
    tags=["views"],
    response_model=List[DataAssetView],
    operation_id="get_data_asset_view"
)
async def get_data_asset_view(
        data_asset_id: int | None = Query(default=None),
        acquisition_id: int | None = Query(default=None),
        subject_id: int | None = Query(default=None),
        data_asset_name: str | None = Query(default=None),
        subject_name: str | None = Query(default=None),
        instrument_name: str | None = Query(default=None),
        data_asset_location: str | None = Query(default=None),
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    statement = select(DataAssetView).offset(offset).limit(limit)
    if data_asset_id is not None:
        statement = statement.where(
            DataAssetView.data_asset_id == data_asset_id
        )
    if acquisition_id is not None:
        statement = statement.where(
            DataAssetView.acquisition_id == acquisition_id
        )
    if subject_id is not None:
        statement = statement.where(
            DataAssetView.subject_id == subject_id
        )
    if data_asset_name is not None:
        statement = statement.where(
            DataAssetView.data_asset_name == data_asset_name
        )
    if instrument_name is not None:
        statement = statement.where(
            DataAssetView.instrument_name == instrument_name
        )
    if subject_name is not None:
        statement = statement.where(
            DataAssetView.subject_name == subject_name
        )
    if data_asset_location is not None:
        statement = statement.where(
            DataAssetView.data_asset_location == data_asset_location
        )
    rows = await session.exec(statement)
    return rows.all()
