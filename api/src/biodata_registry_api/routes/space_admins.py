"""
Auto-generated module to handle endpoint responses for
SpaceAdmins
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.admin import SpaceAdmins, SpaceAdminCreate, SpaceAdminUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post("/space_admin", tags=["space_admins"], response_model=SpaceAdmins)
async def create_space_admin(
        space_admin: SpaceAdminCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = SpaceAdmins.model_validate(space_admin.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get("/space_admin", tags=["space_admins"], response_model=SpaceAdmins)
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

@router.get("/space_admins", tags=["space_admins"], response_model=List[SpaceAdmins])
async def get_space_admins(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(SpaceAdmins).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete("/space_admin", tags=["space_admins"])
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

@router.put("/space_admin", tags=["space_admins"], response_model=SpaceAdmins)
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