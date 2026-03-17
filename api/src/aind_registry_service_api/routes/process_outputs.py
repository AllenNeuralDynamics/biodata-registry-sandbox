"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/process_outputs", tags=["process_outputs"])
async def get_process_outputs(
    data_asset_id: Optional[int] = Query(
        None,
        alias="data_asset_id",
    ),
    process_id: Optional[int] = Query(
        None,
        alias="process_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [data_asset_id, process_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM process_outputs"
    or_statement = ""
    param_dict = dict()
    if data_asset_id is not None:
        or_statement = " WHERE data_asset_id = :data_asset_id"
        param_dict["data_asset_id"] = data_asset_id
    if process_id is not None and not param_dict:
        or_statement = " WHERE process_id = :process_id"
        param_dict["process_id"] = process_id
    elif process_id is not None:
        or_statement = or_statement + " OR process_id = :process_id"
        param_dict["process_id"] = process_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"data_asset_id": row.data_asset_id, "process_id": row.process_id})
    return rows

@router.post("/process_outputs", tags=["process_outputs"])
async def create_process_outputs(
    data_asset_id: int = Query(
        alias="data_asset_id",
    ),
    process_id: int = Query(
        alias="process_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO process_outputs (data_asset_id, process_id) VALUES (:data_asset_id, :process_id) RETURNING *;"
    param_dict = {"data_asset_id": data_asset_id, "process_id": process_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"data_asset_id": row.data_asset_id, "process_id": row.process_id})
    return rows

@router.delete("/process_outputs", tags=["process_outputs"])
async def delete_process_outputs(
    data_asset_id: int = Query(
        alias="data_asset_id",
    ),
    process_id: int = Query(
        alias="process_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM process_outputs WHERE data_asset_id = :space_admin_id AND process_id = :process_id RETURNING *;"
    param_dict = {"data_asset_id": data_asset_id, "process_id": process_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"data_asset_id": row.data_asset_id, "process_id": row.process_id})
    return rows
