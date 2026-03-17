"""Module to handle endpoint responses"""
from typing import Optional, Any, Dict

from fastapi import APIRouter, Depends, status, Query, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import json

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/specimens", tags=["specimens"])
async def get_specimens(
    specimen_id: Optional[int] = Query(
        None,
        alias="specimen_id",
    ),
    schema_id: Optional[int] = Query(
        None,
        alias="schema_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="space_id",
    ),
    subject_id: Optional[int] = Query(
        None,
        alias="subject_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [specimen_id, schema_id, space_id, subject_id, name]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM specimens"
    or_statement = ""
    param_dict = dict()
    if specimen_id is not None:
        or_statement = " WHERE id = :specimen_id"
        param_dict["specimen_id"] = specimen_id
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
    if subject_id is not None and not param_dict:
        or_statement = " WHERE subject_id = :subject_id"
        param_dict["subject_id"] = subject_id
    elif subject_id is not None:
        or_statement = or_statement + " OR subject_id = :subject_id"
        param_dict["subject_id"] = subject_id
    if name is not None and not param_dict:
        or_statement = " WHERE name = :name"
        param_dict["name"] = name
    elif name is not None:
        or_statement = or_statement + " OR name = :name"
        param_dict["name"] = name
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "subject_id": row.subject_id, "name": row.name, "data": row.data})
    return rows

@router.post("/specimens", tags=["specimens"])
async def create_specimens(
    schema_id: int = Query(
        alias="schema_id",
    ),
    space_id: int = Query(
        alias="space_id",
    ),
    subject_id: int = Query(
        alias="subject_id",
    ),
    name: str = Query(
        alias="name",
    ),
    data: Dict[str, Any] = Body(
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO specimens (schema_id, space_id, subject_id, name, data) VALUES (:schema_id, :space_id, :subject_id, :name, :data) RETURNING *;"
    param_dict = {"schema_id": schema_id, "space_id": space_id, "subject_id": subject_id, "name": name, "data": json.dumps(data)}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "subject_id": row.subject_id, "name": row.name, "data": row.data})
    return rows

@router.delete("/specimens", tags=["specimens"])
async def delete_specimens(
    specimen_id: int = Query(
        alias="specimen_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM specimens WHERE id = :specimen_id RETURNING *;"
    param_dict = {"specimen_id": specimen_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "subject_id": row.subject_id, "name": row.name, "data": row.data})
    return rows

@router.put("/specimens", tags=["specimens"])
async def update_specimens(
    specimen_id: int = Query(
        None,
        alias="specimen_id",
    ),
    schema_id: Optional[int] = Query(
        None,
        alias="schema_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="schema_entity_id",
    ),
    subject_id: Optional[int] = Query(
        None,
        alias="subject_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    data: Optional[Dict[str, Any]] = Body(
        None,
        alias="data",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [schema_id, space_id, subject_id, name, data]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE specimens"
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
    if subject_id is not None and not param_dict:
        set_statement = " SET subject_id = :subject_id"
        param_dict["subject_id"] = subject_id
    elif subject_id is not None:
        set_statement = set_statement + ", subject_id = :subject_id"
        param_dict["subject_id"] = subject_id
    if name is not None and not param_dict:
        set_statement = " SET name = :name"
        param_dict["name"] = name
    elif name is not None:
        set_statement = set_statement + ", name = :name"
        param_dict["name"] = name
    if data is not None and not param_dict:
        set_statement = " SET data = :data"
        param_dict["data"] = json.dumps(data)
    elif data is not None:
        set_statement = set_statement + ", data = :data"
        param_dict["data"] = json.dumps(data)
    param_dict["specimen_id"] = specimen_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :specimen_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "schema_id": row.schema_id, "space_id": row.space_id, "subject_id": row.subject_id, "name": row.name, "data": row.data})
    return rows
