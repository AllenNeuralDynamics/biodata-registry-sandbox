"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/organization_admins", tags=["organization_admins"])
async def get_organization_admins(
    organization_admin_id: Optional[int] = Query(
        None,
        alias="organization_admin_id",
    ),
    user_id: Optional[int] = Query(
        None,
        alias="user_id",
    ),
    organization_id: Optional[int] = Query(
        None,
        alias="organization_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [organization_admin_id, user_id, organization_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM organization_admins"
    or_statement = ""
    param_dict = dict()
    if organization_admin_id is not None:
        or_statement = " WHERE id = :organization_admin_id"
        param_dict["organization_admin_id"] = organization_admin_id
    if user_id is not None and not param_dict:
        or_statement = " WHERE user_id = :user_id"
        param_dict["user_id"] = user_id
    elif user_id is not None:
        or_statement = or_statement + " OR user_id = :user_id"
        param_dict["user_id"] = user_id
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
        rows.append({"id": row.id, "user_id": row.user_id, "organization_id": row.organization_id})
    return rows

@router.post("/organization_admins", tags=["organization_admins"])
async def create_organization_admins(
    user_id: int = Query(
        alias="user_id",
    ),
    organization_id: int = Query(
        alias="organization_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO organization_admins (user_id, organization_id) VALUES (:user_id, :organization_id) RETURNING *;"
    param_dict = {"user_id": user_id, "organization_id": organization_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "user_id": row.user_id, "organization_id": row.organization_id})
    return rows

@router.delete("/organization_admins", tags=["organization_admins"])
async def delete_organization_admins(
    organization_admin_id: int = Query(
        alias="organization_admin_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM organization_admins WHERE id = :organization_admin_id RETURNING *;"
    param_dict = {"organization_admin_id": organization_admin_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "user_id": row.user_id, "organization_id": row.organization_id})
    return rows

@router.put("/organization_admins", tags=["organization_admins"])
async def update_organization_admins(
    organization_admin_id: int = Query(
        alias="organization_admin_id",
    ),
    user_id: Optional[int] = Query(
        None,
        alias="user_id",
    ),
    organization_id: Optional[int] = Query(
        None,
        alias="organization_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [user_id, organization_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "UPDATE organization_admins"
    set_statement = ""
    param_dict = dict()
    if user_id is not None:
        set_statement = " SET user_id = :user_id"
        param_dict["user_id"] = user_id
    if organization_id is not None and not param_dict:
        set_statement = " SET organization_id = :organization_id"
        param_dict["organization_id"] = organization_id
    elif organization_id is not None:
        set_statement = set_statement + ", organization_id = :organization_id"
        param_dict["organization_id"] = organization_id
    param_dict["organization_admin_id"] = organization_admin_id
    new_statement = f"{base_statement} {set_statement} WHERE id = :organization_admin_id RETURNING *;"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"id": row.id, "user_id": row.user_id, "organization_id": row.organization_id})
    return rows
