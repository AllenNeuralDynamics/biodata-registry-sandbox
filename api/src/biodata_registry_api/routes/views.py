"""
Module to handle endpoint responses for
DataAssetView
"""

from fastapi import APIRouter, Depends, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from biodata_registry_api.models.views import DataAssetView
from biodata_registry_api.models.crud.views import DataAssetViewsPage, DataAssetViewsFilter

from biodata_registry_api.session import get_session
from biodata_registry_api.routes import encode_next_token, decode_next_token
from fastapi_filter import FilterDepends

router = APIRouter()

@router.get(
    "/data_asset_view",
    tags=["views"],
    response_model=DataAssetViewsPage,
    operation_id="get_data_asset_view"
)
async def get_data_asset_view(
        next_token: str | None = Query(default=None),
        limit: int = Query(default=10, le=100, ge=1),
        filter_query: DataAssetViewsFilter = FilterDepends(DataAssetViewsFilter),
        session: AsyncSession = Depends(get_session),
):
    previous_id = decode_next_token(next_token)
    statement = select(DataAssetView).order_by(DataAssetView.data_asset_id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(DataAssetView.data_asset_id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].data_asset_id)
    return DataAssetViewsPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )
