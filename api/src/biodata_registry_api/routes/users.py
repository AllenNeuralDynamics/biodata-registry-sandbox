"""
Auto-generated module to handle endpoint responses for
Users
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.admin import Users
from biodata_registry_api.models.crud.admin import UserCreate, UserUpdate, UsersPage, UsersFilter
from biodata_registry_api.routes import encode_next_token, decode_next_token

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/user",
    tags=["admin"],
    response_model=Users,
    operation_id="create_user"
)
async def create_user(
        user: UserCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Users.model_validate(user.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/user",
    tags=["admin"],
    response_model=Users,
    operation_id="get_user"
)
async def get_user(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Users, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/users",
    tags=["admin"],
    response_model=UsersPage,
    operation_id="get_users"
)
async def get_users(
        filter_query: UsersFilter = Depends(),
        session: AsyncSession = Depends(get_session),
):
    next_token = filter_query.next_token
    limit = filter_query.limit
    previous_id = decode_next_token(next_token)
    statement = select(Users).order_by(Users.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(Users.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return UsersPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

@router.delete(
    "/user",
    tags=["admin"],
    operation_id="delete_user"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Users, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/user",
    tags=["admin"],
    response_model=Users,
    operation_id="update_user"
)
async def update(
        id: int,
        user: UserUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Users, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in user.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row