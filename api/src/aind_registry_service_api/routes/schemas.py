"""Module to handle endpoint responses"""
from typing import Optional, Any, Dict

from fastapi import APIRouter, Depends, status, Query, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import json

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/schemas", tags=["schemas"])
async def get_schemas(
    schema_id: Optional[int] = Query(
        None,
        alias="schema_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    version: Optional[str] = Query(
        None,
        alias="version",
    ),
    schema_entity_id: Optional[int] = Query(
        None,
        alias="schema_entity_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [schema_id, name, version, schema_entity_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM schemas"
    or_statement = ""
    param_dict = dict()
    if schema_id is not None:
        or_statement = " WHERE id = :schema_id"
        param_dict["schema_id"] = schema_id
    if name is not None and not param_dict:
        or_statement = " WHERE name = :name"
        param_dict["name"] = name
    elif name is not None:
        or_statement = or_statement + " OR name = :name"
        param_dict["name"] = name
    if version is not None and not param_dict:
        or_statement = " WHERE version = :version"
        param_dict["version"] = version
    elif version is not None:
        or_statement = or_statement + " OR version = :version"
        param_dict["version"] = version
    if schema_entity_id is not None and not param_dict:
        or_statement = " WHERE schema_entity_id = :schema_entity_id"
        param_dict["schema_entity_id"] = schema_entity_id
    elif schema_entity_id is not None:
        or_statement = or_statement + " OR schema_entity_id = :schema_entity_id"
        param_dict["schema_entity_id"] = schema_entity_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "version": row.version, "schema_entity_id": row.schema_entity_id, "data": row.data})
    return rows

@router.post("/schemas", tags=["schemas"])
async def create_schemas(
    name: str = Query(
        alias="name",
    ),
    version: str = Query(
        alias="version",
    ),
    schema_entity_id: int = Query(
        alias="schema_entity_id",
    ),
    data: Dict[str, Any] = Body(
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO schemas (name, version, schema_entity_id, data) VALUES (:name, :version, :schema_entity_id, :data) RETURNING *;"
    param_dict = {"name": name, "version": version, "schema_entity_id": schema_entity_id, "data": json.dumps(data)}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "version": row.version, "schema_entity_id": row.schema_entity_id, "data": row.data})
    return rows

@router.delete("/schemas", tags=["schemas"])
async def delete_schemas(
    schema_id: int = Query(
        alias="schema_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM schemas WHERE id = :schema_id RETURNING *;"
    param_dict = {"schema_id": schema_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "version": row.version, "schema_entity_id": row.schema_entity_id, "data": row.data})
    return rows

@router.put("/schemas", tags=["schemas"])
async def update_schemas(
    schema_id: int = Query(
        None,
        alias="schema_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    version: Optional[str] = Query(
        None,
        alias="version",
    ),
    schema_entity_id: Optional[int] = Query(
        None,
        alias="schema_entity_id",
    ),
    data: Optional[Dict[str, Any]] = Body(
        None,
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [name, version, schema_entity_id, data]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE schemas"
    set_statement = ""
    param_dict = dict()
    if name is not None:
        set_statement = " SET name = :name"
        param_dict["name"] = name
    if version is not None and not param_dict:
        set_statement = " SET version = :version"
        param_dict["version"] = version
    elif version is not None:
        set_statement = set_statement + ", version = :version"
        param_dict["version"] = version
    if schema_entity_id is not None and not param_dict:
        set_statement = " SET schema_entity_id = :schema_entity_id"
        param_dict["schema_entity_id"] = schema_entity_id
    elif schema_entity_id is not None:
        set_statement = set_statement + ", schema_entity_id = :schema_entity_id"
        param_dict["schema_entity_id"] = schema_entity_id
    if data is not None and not param_dict:
        set_statement = " SET data = :data"
        param_dict["data"] = json.dumps(data)
    elif data is not None:
        set_statement = set_statement + ", data = :data"
        param_dict["data"] = json.dumps(data)
    param_dict["schema_id"] = schema_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :schema_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "version": row.version, "schema_entity_id": row.schema_entity_id, "data": row.data})
    return rows
