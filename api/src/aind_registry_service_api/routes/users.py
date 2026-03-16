"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/users", tags=["users"])
async def get_users(
    user_id: Optional[int] = Query(
        None,
        alias="user_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    contact: Optional[str] = Query(
        None,
        alias="contact",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [user_id, name, contact]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM users"
    or_statement = ""
    param_dict = dict()
    if user_id is not None:
        or_statement = " WHERE id = :user_id"
        param_dict["user_id"] = user_id
    if name is not None and not param_dict:
        or_statement = " WHERE name = :name"
        param_dict["name"] = name
    elif name is not None:
        or_statement = or_statement + " OR name = :name"
        param_dict["name"] = name
    if contact is not None and not param_dict:
        or_statement = " WHERE contact = :contact"
        param_dict["contact"] = contact
    elif contact is not None:
        or_statement = or_statement + " OR contact = :contact"
        param_dict["contact"] = contact
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "contact": row.contact})
    return rows

@router.post("/users", tags=["users"])
async def create_users(
    name: str = Query(
        alias="name",
    ),
    contact: str = Query(
        alias="contact",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO users (name, contact) VALUES (:name, :contact) RETURNING *;"
    param_dict = {"name": name, "contact": contact}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "contact": row.contact})
    return rows

@router.delete("/users", tags=["users"])
async def delete_users(
    user_id: int = Query(
        alias="user_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM users WHERE id = :user_id RETURNING *;"
    param_dict = {"user_id": user_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "contact": row.contact})
    return rows

@router.put("/users", tags=["users"])
async def update_users(
    user_id: int = Query(
        alias="user_id",
    ),
    name: Optional[str] = Query(
        None,
        alias="name",
    ),
    contact: Optional[str] = Query(
        None,
        alias="contact",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [name, contact]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE users"
    set_statement = ""
    param_dict = dict()
    if name is not None:
        set_statement = " SET name = :name"
        param_dict["name"] = name
    if contact is not None and not param_dict:
        set_statement = " SET contact = :contact"
        param_dict["contact"] = contact
    elif contact is not None:
        set_statement = set_statement + ", contact = :contact"
        param_dict["contact"] = contact
    param_dict["user_id"] = user_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :user_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "name": row.name, "contact": row.contact})
    return rows
