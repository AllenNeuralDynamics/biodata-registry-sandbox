"""Module to handle endpoint responses"""
from typing import Optional, Any, Dict

from fastapi import APIRouter, Depends, status, Query, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import json

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/data_assets", tags=["data_assets"])
async def get_data_assets(
    data_asset_id: Optional[int] = Query(
        None,
        alias="data_asset_id",
    ),
    schema_id: Optional[int] = Query(
        None,
        alias="schema_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="space_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    location: Optional[str] = Query(
        None,
        alias="location",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [data_asset_id, schema_id, space_id, name, location]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM data_assets"
    or_statement = ""
    param_dict = dict()
    if data_asset_id is not None:
        or_statement = " WHERE id = :data_asset_id"
        param_dict["data_asset_id"] = data_asset_id
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
    if name is not None and not param_dict:
        or_statement = " WHERE name = :name"
        param_dict["name"] = name
    elif name is not None:
        or_statement = or_statement + " OR name = :name"
        param_dict["name"] = name
    if location is not None and not param_dict:
        or_statement = " WHERE location = :location"
        param_dict["location"] = location
    elif name is not None:
        or_statement = or_statement + " OR location = :location"
        param_dict["location"] = location
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "name": row.name, "location": row.location, "data": row.data})
    return rows

@router.post("/data_assets", tags=["data_assets"])
async def create_data_assets(
    schema_id: int = Query(
        alias="schema_id",
    ),
    space_id: int = Query(
        alias="space_id",
    ),
    name: str = Query(
        alias="name",
    ),
    location: str = Query(
        alias="location",
    ),
    data: Dict[str, Any] = Body(
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO data_assets (schema_id, space_id, name, location, data) VALUES (:schema_id, :space_id, :name, :location, :data) RETURNING *;"
    param_dict = {"schema_id": schema_id, "space_id": space_id, "name": name, "location": location, "data": json.dumps(data)}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "name": row.name, "location": row.location, "data": row.data})
    return rows

@router.delete("/data_assets", tags=["data_assets"])
async def delete_data_assets(
    data_asset_id: int = Query(
        alias="data_asset_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM data_assets WHERE id = :data_asset_id RETURNING *;"
    param_dict = {"data_asset_id": data_asset_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "name": row.name, "location": row.location, "data": row.data})
    return rows

@router.put("/data_assets", tags=["data_assets"])
async def update_data_assets(
    data_asset_id: int = Query(
        None,
        alias="data_asset_id",
    ),
    schema_id: Optional[int] = Query(
        None,
        alias="schema_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="schema_entity_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    location: Optional[str] = Query(
        None,
        alias="location",
    ),
    data: Optional[Dict[str, Any]] = Body(
        None,
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [schema_id, space_id, name, location, data]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE data_assets"
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
    if name is not None and not param_dict:
        set_statement = " SET name = :name"
        param_dict["name"] = name
    elif name is not None:
        set_statement = set_statement + ", name = :name"
        param_dict["name"] = name
    if location is not None and not param_dict:
        set_statement = " SET location = :location"
        param_dict["location"] = location
    elif location is not None:
        set_statement = set_statement + ", location = :location"
        param_dict["location"] = location
    if data is not None and not param_dict:
        set_statement = " SET data = :data"
        param_dict["data"] = json.dumps(data)
    elif data is not None:
        set_statement = set_statement + ", data = :data"
        param_dict["data"] = json.dumps(data)
    param_dict["data_asset_id"] = data_asset_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :data_asset_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "name": row.name, "location": row.location, "data": row.data})
    return rows
