"""
Auto-generated module to handle endpoint responses for
Spaces
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.admin import Spaces, SpaceCreate, SpaceUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post("/space", tags=["spaces"], response_model=Spaces)
async def create_space(
        space: SpaceCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Spaces.model_validate(space.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get("/space", tags=["spaces"], response_model=Spaces)
async def get_space(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Spaces, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get("/spaces", tags=["spaces"], response_model=List[Spaces])
async def get_spaces(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Spaces).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete("/space", tags=["spaces"])
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Spaces, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put("/space", tags=["spaces"], response_model=Spaces)
async def update(
        id: int,
        space: SpaceUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Spaces, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in space.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row