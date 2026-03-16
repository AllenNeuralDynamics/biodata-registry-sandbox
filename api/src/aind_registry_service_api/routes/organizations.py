"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/organizations", tags=["organizations"])
async def get_organizations(
    organization_id: Optional[int] = Query(
        None,
        alias="organization_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [organization_id, name]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM organizations"
    or_statement = ""
    param_dict = dict()
    if organization_id is not None:
        or_statement = " WHERE id = :organization_id"
        param_dict["organization_id"] = organization_id
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

@router.post("/organizations", tags=["organizations"])
async def create_organizations(
    name: str = Query(
        alias="name",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO organizations (name) VALUES (:name) RETURNING *;"
    param_dict = {"name": name}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name})
    return rows

@router.delete("/organizations", tags=["organizations"])
async def delete_organizations(
    organization_id: int = Query(
        alias="organization_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM organizations WHERE id = :organization_id RETURNING *;"
    param_dict = {"organization_id": organization_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name})
    return rows

@router.put("/organizations", tags=["organizations"])
async def update_organizations(
    organization_id: int = Query(
        alias="organization_id",
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
    base_statement = "UPDATE organizations"
    set_statement = ""
    param_dict = dict()
    if name is not None:
        set_statement = " SET name = :name"
        param_dict["name"] = name
    param_dict["organization_id"] = organization_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :organization_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name})
    return rows
