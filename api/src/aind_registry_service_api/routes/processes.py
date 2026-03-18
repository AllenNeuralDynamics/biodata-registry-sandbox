"""Module to handle endpoint responses"""
from typing import Optional, Any, Dict

from fastapi import APIRouter, Depends, status, Query, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import json

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/processes", tags=["processes"])
async def get_processes(
    process_id: Optional[int] = Query(
        None,
        alias="process_id",
    ),
    schema_id: Optional[int] = Query(
        None,
        alias="schema_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="space_id",
    ),
    output_data_asset_id: Optional[int] = Query(
        None,
        alias="output_data_asset_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [process_id, schema_id, space_id, output_data_asset_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM processes"
    or_statement = ""
    param_dict = dict()
    if process_id is not None:
        or_statement = " WHERE id = :process_id"
        param_dict["process_id"] = process_id
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
    if output_data_asset_id is not None and not param_dict:
        or_statement = " WHERE output_data_asset_id = :output_data_asset_id"
        param_dict["output_data_asset_id"] = output_data_asset_id
    elif output_data_asset_id is not None:
        or_statement = or_statement + " OR output_data_asset_id = :output_data_asset_id"
        param_dict["output_data_asset_id"] = output_data_asset_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "output_data_asset_id": row.output_data_asset_id, "data": row.data})
    return rows

@router.post("/processes", tags=["processes"])
async def create_processes(
    schema_id: int = Query(
        alias="schema_id",
    ),
    space_id: int = Query(
        alias="space_id",
    ),
    output_data_asset_id: int = Query(
        alias="output_data_asset_id",
    ),
    data: Dict[str, Any] = Body(
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO processes (schema_id, space_id, output_data_asset_id, data) VALUES (:schema_id, :space_id, :output_data_asset_id, :data) RETURNING *;"
    param_dict = {"schema_id": schema_id, "space_id": space_id, "output_data_asset_id": output_data_asset_id, "data": json.dumps(data)}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "output_data_asset_id": row.output_data_asset_id, "data": row.data})
    return rows

@router.delete("/processes", tags=["processes"])
async def delete_processes(
    process_id: int = Query(
        alias="process_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM processes WHERE id = :process_id RETURNING *;"
    param_dict = {"process_id": process_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "output_data_asset_id": row.output_data_asset_id, "data": row.data})
    return rows

@router.put("/processes", tags=["processes"])
async def update_processes(
    process_id: int = Query(
        None,
        alias="process_id",
    ),
    schema_id: Optional[int] = Query(
        None,
        alias="schema_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="schema_entity_id",
    ),
    output_data_asset_id: Optional[int] = Query(
        None,
        alias="output_data_asset_id",
    ),
    data: Optional[Dict[str, Any]] = Body(
        None,
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [schema_id, space_id, output_data_asset_id, data]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE processes"
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
    if output_data_asset_id is not None and not param_dict:
        set_statement = " SET output_data_asset_id = :output_data_asset_id"
        param_dict["output_data_asset_id"] = output_data_asset_id
    elif output_data_asset_id is not None:
        set_statement = set_statement + ", output_data_asset_id = :output_data_asset_id"
        param_dict["output_data_asset_id"] = output_data_asset_id
    if data is not None and not param_dict:
        set_statement = " SET data = :data"
        param_dict["data"] = json.dumps(data)
    elif data is not None:
        set_statement = set_statement + ", data = :data"
        param_dict["data"] = json.dumps(data)
    param_dict["process_id"] = process_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :process_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "output_data_asset_id": row.output_data_asset_id, "data": row.data})
    return rows
