"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/collections", tags=["collections"])
async def get_collections(
    collection_id: Optional[int] = Query(
        None,
        alias="collection_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    description: Optional[str] = Query(
        None,
        alias="description",
    ),
    owner_id: Optional[int] = Query(
        None,
        alias="owner_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [collection_id, name, description, owner_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM collections"
    or_statement = ""
    param_dict = dict()
    if collection_id is not None:
        or_statement = " WHERE id = :collection_id"
        param_dict["collection_id"] = collection_id
    if name is not None and not param_dict:
        or_statement = " WHERE name = :name"
        param_dict["name"] = name
    elif name is not None:
        or_statement = or_statement + " OR name = :name"
        param_dict["name"] = name
    if description is not None and not param_dict:
        or_statement = " WHERE description = :description"
        param_dict["description"] = description
    elif description is not None:
        or_statement = or_statement + " OR description = :description"
        param_dict["description"] = description
    if owner_id is not None and not param_dict:
        or_statement = " WHERE owner_id = :owner_id"
        param_dict["owner_id"] = owner_id
    elif owner_id is not None:
        or_statement = or_statement + " OR owner_id = :owner_id"
        param_dict["owner_id"] = owner_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "description": row.description, "owner_id": row.owner_id})
    return rows

@router.post("/collections", tags=["collections"])
async def create_collections(
    name: str = Query(
        alias="name",
    ),
    description: str = Query(
        alias="description",
    ),
    owner_id: Optional[int] = Query(
        None,
        alias="owner_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO collections (name, description, owner_id) VALUES (:name, :description, :owner_id) RETURNING *;"
    param_dict = {"name": name, "description": description, "owner_id": owner_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "description": row.description, "owner_id": row.owner_id})
    return rows

@router.delete("/collections", tags=["collections"])
async def delete_collections(
    collection_id: int = Query(
        alias="collection_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM collections WHERE id = :collection_id RETURNING *;"
    param_dict = {"collection_id": collection_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "description": row.description, "owner_id": row.owner_id})
    return rows

@router.put("/collections", tags=["collections"])
async def update_collections(
    collection_id: int = Query(
        alias="collection_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    description: Optional[str] = Query(
        None,
        alias="description",
    ),
    owner_id: Optional[int] = Query(
        None,
        alias="owner_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [name, description, owner_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE collections"
    set_statement = ""
    param_dict = dict()
    if name is not None:
        set_statement = " SET name = :name"
        param_dict["name"] = name
    if description is not None and not param_dict:
        set_statement = " SET description = :description"
        param_dict["description"] = description
    elif description is not None:
        set_statement = set_statement + ", description = :description"
        param_dict["description"] = description
    if owner_id is not None and not param_dict:
        set_statement = " SET owner_id = :owner_id"
        param_dict["owner_id"] = owner_id
    elif owner_id is not None:
        set_statement = set_statement + ", owner_id = :owner_id"
        param_dict["owner_id"] = owner_id
    param_dict["collection_id"] = collection_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :collection_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "description": row.description, "owner_id": row.owner_id})
    return rows
