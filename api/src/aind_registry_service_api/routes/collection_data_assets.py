"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/collection_data_assets", tags=["collection_data_assets"])
async def get_collection_data_assets(
    collection_id: Optional[int] = Query(
        None,
        alias="collection_id",
    ),
    data_asset_id: Optional[int] = Query(
        None,
        alias="data_asset_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [collection_id, data_asset_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM collection_data_assets"
    or_statement = ""
    param_dict = dict()
    if collection_id is not None:
        or_statement = " WHERE collection_id = :collection_id"
        param_dict["collection_id"] = collection_id
    if data_asset_id is not None and not param_dict:
        or_statement = " WHERE data_asset_id = :data_asset_id"
        param_dict["data_asset_id"] = data_asset_id
    elif data_asset_id is not None:
        or_statement = or_statement + " OR data_asset_id = :data_asset_id"
        param_dict["data_asset_id"] = data_asset_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"collection_id": row.collection_id, "data_asset_id": row.data_asset_id})
    return rows

@router.post("/collection_data_assets", tags=["collection_data_assets"])
async def create_collection_data_assets(
    collection_id: int = Query(
        alias="collection_id",
    ),
    data_asset_id: int = Query(
        alias="data_asset_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO collection_data_assets (collection_id, data_asset_id) VALUES (:collection_id, :data_asset_id) RETURNING *;"
    param_dict = {"collection_id": collection_id, "data_asset_id": data_asset_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"collection_id": row.collection_id, "data_asset_id": row.data_asset_id})
    return rows

@router.delete("/collection_data_assets", tags=["collection_data_assets"])
async def delete_collection_data_assets(
    collection_id: int = Query(
        alias="collection_id",
    ),
    data_asset_id: int = Query(
        alias="data_asset_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM collection_data_assets WHERE collection_id = :space_admin_id AND data_asset_id = :data_asset_id RETURNING *;"
    param_dict = {"collection_id": collection_id, "data_asset_id": data_asset_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"collection_id": row.collection_id, "data_asset_id": row.data_asset_id})
    return rows
