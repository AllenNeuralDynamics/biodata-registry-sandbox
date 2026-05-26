"""
Auto-generated module to handle endpoint responses for
DataAssets
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from biodata_registry_api.models.admin import Collections
from biodata_registry_api.models.crud.core import DataAssetCreate, DataAssetUpdate, DataAssetsPage, DataAssetsFilter
from biodata_registry_api.models.core import DataAssets, Processes

from biodata_registry_api.session import get_session
from biodata_registry_api.routes import encode_next_token, decode_next_token

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
    response_model=DataAssetsPage,
    operation_id="get_data_assets"
)
async def get_data_assets(
        filter_query: DataAssetsFilter = Depends(),
        session: AsyncSession = Depends(get_session),
):
    next_token = filter_query.next_token
    limit = filter_query.limit
    previous_id = decode_next_token(next_token)
    statement = select(DataAssets).order_by(DataAssets.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(DataAssets.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return DataAssetsPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

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
    for k, v in data_asset.model_dump(
            exclude_unset=True, exclude={'collections'}
    ).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row

@router.get(
    "/data_asset_collections",
    tags=["core"],
    response_model=List[Collections],
    operation_id="get_data_asset_collections"
)
async def get_data_asset_collections(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(DataAssets, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    collections = row.collections
    return collections

@router.delete(
    "/data_asset_collection",
    tags=["core"],
    operation_id="remove_data_asset_collection"
)
async def remove_collection_data_asset(
        id: int,
        collection_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(DataAssets, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Collections, collection_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{collection_id} not found!"
        )
    row.collections.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Removed collection {collection_id} from data_asset {id}"
    }

@router.put(
    "/data_asset_collection",
    tags=["core"],
    operation_id="put_data_asset_collection"
)
async def add_data_asset_collection(
        id: int,
        collection_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(DataAssets, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Collections, collection_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{collection_id} not found!"
        )
    row.collections.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Added collection {collection_id} to data_asset {id}"
    }

@router.get(
    "/data_asset_process_inputs",
    tags=["core"],
    response_model=List[Processes],
    operation_id="get_data_asset_process_inputs"
)
async def get_data_asset_process_inputs(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(DataAssets, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    process_inputs = row.process_inputs
    return process_inputs

@router.delete(
    "/data_asset_process_input",
    tags=["core"],
    operation_id="remove_data_asset_process_input"
)
async def remove_data_asset_process_input(
        id: int,
        process_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(DataAssets, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Processes, process_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{process_id} not found!"
        )
    row.process_inputs.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Removed process_input {process_id} from data_asset {id}"
    }

@router.put(
    "/data_asset_process_input",
    tags=["core"],
    operation_id="put_data_asset_process_input"
)
async def add_data_asset_process_input(
        id: int,
        process_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(DataAssets, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Processes, process_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{process_id} not found!"
        )
    row.process_inputs.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Added process_input {process_id} to data_asset {id}"
    }