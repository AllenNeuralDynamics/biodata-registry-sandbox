"""
Auto-generated module to handle endpoint responses for
SpaceAdmins
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.crud.admin import SpaceAdminCreate, SpaceAdminUpdate, SpaceAdminsPage, SpaceAdminsFilter
from biodata_registry_api.models.admin import SpaceAdmins

from biodata_registry_api.session import get_session

from biodata_registry_api.routes import encode_next_token, decode_next_token
from fastapi_filter import FilterDepends

router = APIRouter()

@router.post(
    "/space_admin",
    tags=["admin"],
    response_model=SpaceAdmins,
    operation_id="create_space_admin"
)
async def create_space_admin(
        space_admin: SpaceAdminCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = SpaceAdmins.model_validate(space_admin.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/space_admin",
    tags=["admin"],
    response_model=SpaceAdmins,
    operation_id="get_space_admin"
)
async def get_space_admin(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpaceAdmins, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/space_admins",
    tags=["admin"],
    response_model=SpaceAdminsPage,
    operation_id="get_space_admins"
)
async def get_space_admins(
        next_token: str | None = Query(default=None),
        limit: int = Query(default=10, le=100, ge=1),
        filter_query: SpaceAdminsFilter = FilterDepends(SpaceAdminsFilter),
        session: AsyncSession = Depends(get_session),
):
    previous_id = decode_next_token(next_token)
    statement = select(SpaceAdmins).order_by(SpaceAdmins.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(SpaceAdmins.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return SpaceAdminsPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

@router.delete(
    "/space_admin",
    tags=["admin"],
    operation_id="delete_space_admin"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpaceAdmins, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/space_admin",
    tags=["admin"],
    response_model=SpaceAdmins,
    operation_id="update_space_admin"
)
async def update(
        id: int,
        space_admin: SpaceAdminUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpaceAdmins, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in space_admin.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row