"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/spaces", tags=["spaces"])
async def get_spaces(
    space_id: Optional[int] = Query(
        None,
        alias="space_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    organization_id: Optional[int] = Query(
        None,
        alias="organization_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [space_id, name, organization_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM spaces"
    or_statement = ""
    param_dict = dict()
    if space_id is not None:
        or_statement = " WHERE id = :space_id"
        param_dict["space_id"] = space_id
    if name is not None and not param_dict:
        or_statement = " WHERE name = :name"
        param_dict["name"] = name
    elif name is not None:
        or_statement = or_statement + " OR name = :name"
        param_dict["name"] = name
    if organization_id is not None and not param_dict:
        or_statement = " WHERE organization_id = :organization_id"
        param_dict["organization_id"] = organization_id
    elif organization_id is not None:
        or_statement = or_statement + " OR organization_id = :organization_id"
        param_dict["organization_id"] = organization_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "organization_id": row.organization_id})
    return rows

@router.post("/spaces", tags=["spaces"])
async def create_spaces(
    name: str = Query(
        alias="name",
    ),
    organization_id: int = Query(
        alias="organization_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO spaces (name, organization_id) VALUES (:name, :organization_id) RETURNING *;"
    param_dict = {"name": name, "organization_id": organization_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "organization_id": row.organization_id})
    return rows

@router.delete("/spaces", tags=["spaces"])
async def delete_spaces(
    space_id: int = Query(
        alias="space_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM spaces WHERE id = :space_id RETURNING *;"
    param_dict = {"space_id": space_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "organization_id": row.organization_id})
    return rows

@router.put("/spaces", tags=["spaces"])
async def update_spaces(
    space_id: int = Query(
        alias="space_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    organization_id: Optional[int] = Query(
        None,
        alias="organization_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [name, organization_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE spaces"
    set_statement = ""
    param_dict = dict()
    if name is not None:
        set_statement = " SET name = :name"
        param_dict["name"] = name
    if organization_id is not None and not param_dict:
        set_statement = " SET organization_id = :organization_id"
        param_dict["organization_id"] = organization_id
    elif organization_id is not None:
        set_statement = set_statement + ", organization_id = :organization_id"
        param_dict["organization_id"] = organization_id
    param_dict["space_id"] = space_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :space_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "organization_id": row.organization_id})
    return rows
