"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/space_admins", tags=["space_admins"])
async def get_space_admins(
    space_admin_id: Optional[int] = Query(
        None,
        alias="space_admin_id",
    ),
    user_id: Optional[int] = Query(
        None,
        alias="user_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="space_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [space_admin_id, user_id, space_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM space_admins"
    or_statement = ""
    param_dict = dict()
    if space_admin_id is not None:
        or_statement = " WHERE id = :space_admin_id"
        param_dict["space_admin_id"] = space_admin_id
    if user_id is not None and not param_dict:
        or_statement = " WHERE user_id = :user_id"
        param_dict["user_id"] = user_id
    elif user_id is not None:
        or_statement = or_statement + " OR user_id = :user_id"
        param_dict["user_id"] = user_id
    if space_id is not None and not param_dict:
        or_statement = " WHERE space_id = :space_id"
        param_dict["space_id"] = space_id
    elif space_id is not None:
        or_statement = or_statement + " OR space_id = :space_id"
        param_dict["space_id"] = space_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "user_id": row.user_id, "space_id": row.space_id})
    return rows

@router.post("/space_admins", tags=["space_admins"])
async def create_space_admins(
    user_id: int = Query(
        alias="user_id",
    ),
    space_id: int = Query(
        alias="space_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO space_admins (user_id, space_id) VALUES (:user_id, :space_id) RETURNING *;"
    param_dict = {"user_id": user_id, "space_id": space_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "user_id": row.user_id, "space_id": row.space_id})
    return rows

@router.delete("/space_admins", tags=["space_admins"])
async def delete_space_admins(
    space_admin_id: int = Query(
        alias="space_admin_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM space_admins WHERE id = :space_admin_id RETURNING *;"
    param_dict = {"space_admin_id": space_admin_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "user_id": row.user_id, "space_id": row.space_id})
    return rows

@router.put("/space_admins", tags=["space_admins"])
async def update_space_admins(
    space_admin_id: int = Query(
        alias="space_admin_id",
    ),
    user_id: Optional[int] = Query(
        None,
        alias="user_id",
    ),
    space_id: Optional[int] = Query(
        None,
        alias="space_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [user_id, space_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE space_admins"
    set_statement = ""
    param_dict = dict()
    if user_id is not None:
        set_statement = " SET user_id = :user_id"
        param_dict["user_id"] = user_id
    if space_id is not None and not param_dict:
        set_statement = " SET space_id = :space_id"
        param_dict["space_id"] = space_id
    elif space_id is not None:
        set_statement = set_statement + ", space_id = :space_id"
        param_dict["space_id"] = space_id
    param_dict["space_admin_id"] = space_admin_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :space_admin_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "user_id": row.user_id, "space_id": row.space_id})
    return rows
