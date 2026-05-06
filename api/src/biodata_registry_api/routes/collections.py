"""
Auto-generated module to handle endpoint responses for
Collections
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.admin import Collections, CollectionCreate, CollectionUpdate
from biodata_registry_api.models.core import DataAssets

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/collection",
    tags=["admin"],
    response_model=Collections,
    operation_id="create_collection"
)
async def create_collection(
        collection: CollectionCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Collections.model_validate(collection.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/collection",
    tags=["admin"],
    response_model=Collections,
    operation_id="get_collection"
)
async def get_collection(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Collections, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/collections",
    tags=["admin"],
    response_model=List[Collections],
    operation_id="get_collections"
)
async def get_collections(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Collections).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete(
    "/collection",
    tags=["admin"],
    operation_id="delete_collection"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Collections, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/collection",
    tags=["admin"],
    response_model=Collections,
    operation_id="update_collection"
)
async def update(
        id: int,
        collection: CollectionUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Collections, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in collection.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row

@router.get(
    "/collection_data_assets",
    tags=["admin"],
    response_model=List[DataAssets],
    operation_id="get_collection_data_assets"
)
async def get_collection_data_assets(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Collections, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    data_assets = row.data_assets
    return data_assets

@router.delete(
    "/collection_data_asset",
    tags=["admin"],
    operation_id="remove_collection_data_asset"
)
async def remove_collection_data_asset(
        id: int,
        data_asset_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Collections, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(DataAssets, data_asset_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{data_asset_id} not found!"
        )
    row.data_assets.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Removed data_asset {data_asset_id} from collection {id}"
    }

@router.put(
    "/collection_data_asset",
    tags=["admin"],
    operation_id="put_collection_data_asset"
)
async def add_collection_data_asset(
        id: int,
        data_asset_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Collections, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(DataAssets, data_asset_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{data_asset_id} not found!"
        )
    row.data_assets.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Added data_asset {data_asset_id} to collection {id}"
    }
