"""
Auto-generated module to handle endpoint responses for
DataAssets
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import DataAssets, DataAssetCreate, DataAssetUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/data_asset",
    tags=["core"],
    response_model=DataAssets,
    operation_id="create_data_asset"
)
async def create_data_asset(
        data_asset: DataAssetCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = DataAssets.model_validate(data_asset.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/data_asset",
    tags=["core"],
    response_model=DataAssets,
    operation_id="get_data_asset"
)
async def get_data_asset(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(DataAssets, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/data_assets",
    tags=["core"],
    response_model=List[DataAssets],
    operation_id="get_data_assets"
)
async def get_data_assets(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(DataAssets).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete(
    "/data_asset",
    tags=["core"],
    operation_id="delete_data_asset"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(DataAssets, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/data_asset",
    tags=["core"],
    response_model=DataAssets,
    operation_id="update_data_asset"
)
async def update(
        id: int,
        data_asset: DataAssetUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(DataAssets, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in data_asset.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row