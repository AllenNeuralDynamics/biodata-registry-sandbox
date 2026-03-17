"""Module to handle endpoint responses"""
from typing import Optional, Any, Dict

from fastapi import APIRouter, Depends, status, Query, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import json

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/quality_control", tags=["quality_control"])
async def get_quality_control(
    quality_control_id: Optional[int] = Query(
        None,
        alias="quality_control_id",
    ),
    schema_id: Optional[int] = Query(
        None,
        alias="schema_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="space_id",
    ),
    data_asset_id: Optional[int] = Query(
        None,
        alias="data_asset_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [quality_control_id, schema_id, space_id, data_asset_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM quality_control"
    or_statement = ""
    param_dict = dict()
    if quality_control_id is not None:
        or_statement = " WHERE id = :quality_control_id"
        param_dict["quality_control_id"] = quality_control_id
    if schema_id is not None and not param_dict:
        or_statement = " WHERE schema_id = :schema_id"
        param_dict["schema_id"] = schema_id
    elif schema_id is not None:
        or_statement = or_statement + " OR schema_id = :schema_id"
        param_dict["schema_id"] = schema_id
    if space_id is not None and not param_dict:
        or_statement = " WHERE space_id = :space_id"
        param_dict["space_id"] = space_id
    elif space_id is not None:
        or_statement = or_statement + " OR space_id = :space_id"
        param_dict["space_id"] = space_id
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
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "data_asset_id": row.data_asset_id, "data": row.data})
    return rows

@router.post("/quality_control", tags=["quality_control"])
async def create_quality_control(
    schema_id: int = Query(
        alias="schema_id",
    ),
    space_id: int = Query(
        alias="space_id",
    ),
    data_asset_id: int = Query(
        alias="data_asset_id",
    ),
    data: Dict[str, Any] = Body(
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO quality_control (schema_id, space_id, data_asset_id, data) VALUES (:schema_id, :space_id, :data_asset_id, :data) RETURNING *;"
    param_dict = {"schema_id": schema_id, "space_id": space_id, "data_asset_id": data_asset_id, "data": json.dumps(data)}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "data_asset_id": row.data_asset_id, "data": row.data})
    return rows

@router.delete("/quality_control", tags=["quality_control"])
async def delete_quality_control(
    quality_control_id: int = Query(
        alias="quality_control_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM quality_control WHERE id = :quality_control_id RETURNING *;"
    param_dict = {"quality_control_id": quality_control_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "data_asset_id": row.data_asset_id, "data": row.data})
    return rows

@router.put("/quality_control", tags=["quality_control"])
async def update_quality_control(
    quality_control_id: int = Query(
        None,
        alias="quality_control_id",
    ),
    schema_id: Optional[int] = Query(
        None,
        alias="schema_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="schema_entity_id",
    ),
    data_asset_id: Optional[int] = Query(
        None,
        alias="data_asset_id",
    ),
    data: Optional[Dict[str, Any]] = Body(
        None,
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [schema_id, space_id, data_asset_id, data]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE quality_control"
    set_statement = ""
    param_dict = dict()
    if schema_id is not None:
        set_statement = " SET schema_id = :schema_id"
        param_dict["schema_id"] = schema_id
    if space_id is not None and not param_dict:
        set_statement = " SET space_id = :space_id"
        param_dict["space_id"] = space_id
    elif space_id is not None:
        set_statement = set_statement + ", space_id = :space_id"
        param_dict["space_id"] = space_id
    if data_asset_id is not None and not param_dict:
        set_statement = " SET data_asset_id = :data_asset_id"
        param_dict["data_asset_id"] = data_asset_id
    elif data_asset_id is not None:
        set_statement = set_statement + ", data_asset_id = :data_asset_id"
        param_dict["data_asset_id"] = data_asset_id
    if data is not None and not param_dict:
        set_statement = " SET data = :data"
        param_dict["data"] = json.dumps(data)
    elif data is not None:
        set_statement = set_statement + ", data = :data"
        param_dict["data"] = json.dumps(data)
    param_dict["quality_control_id"] = quality_control_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :quality_control_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "data_asset_id": row.data_asset_id, "data": row.data})
    return rows
