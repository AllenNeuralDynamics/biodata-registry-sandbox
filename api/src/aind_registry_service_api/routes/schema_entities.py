"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/schema_entities", tags=["schema_entities"])
async def get_schema_entities(
    schema_entity_id: Optional[int] = Query(
        None,
        alias="schema_entity_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [schema_entity_id, name]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM schema_entities"
    or_statement = ""
    param_dict = dict()
    if schema_entity_id is not None:
        or_statement = " WHERE id = :schema_entity_id"
        param_dict["schema_entity_id"] = schema_entity_id
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
        rows.append({"id": row.id, "name": row.name})
    return rows

@router.post("/schema_entities", tags=["schema_entities"])
async def create_schema_entities(
    name: str = Query(
        alias="name",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO schema_entities (name) VALUES (:name) RETURNING *;"
    param_dict = {"name": name}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name})
    return rows

@router.delete("/schema_entities", tags=["schema_entities"])
async def delete_schema_entities(
    schema_entity_id: int = Query(
        alias="schema_entity_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM schema_entities WHERE id = :schema_entity_id RETURNING *;"
    param_dict = {"schema_entity_id": schema_entity_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name})
    return rows

@router.put("/schema_entities", tags=["schema_entities"])
async def update_schema_entities(
    schema_entity_id: int = Query(
        alias="schema_entity_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [name]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE schema_entities"
    set_statement = ""
    param_dict = dict()
    if name is not None:
        set_statement = " SET name = :name"
        param_dict["name"] = name
    param_dict["schema_entity_id"] = schema_entity_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :schema_entity_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name})
    return rows
