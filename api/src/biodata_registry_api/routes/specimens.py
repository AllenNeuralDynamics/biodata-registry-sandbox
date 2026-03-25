"""
Auto-generated module to handle endpoint responses for
Specimens
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Specimens, SpecimenCreate, SpecimenUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/specimen",
    tags=["core"],
    response_model=Specimens,
    operation_id="create_specimen"
)
async def create_specimen(
        specimen: SpecimenCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Specimens.model_validate(specimen.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/specimen",
    tags=["core"],
    response_model=Specimens,
    operation_id="get_specimen"
)
async def get_specimen(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/specimens",
    tags=["core"],
    response_model=List[Specimens],
    operation_id="get_specimens"
)
async def get_specimens(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Specimens).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete(
    "/specimen",
    tags=["core"],
    operation_id="delete_specimen"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/specimen",
    tags=["core"],
    response_model=Specimens,
    operation_id="update_specimen"
)
async def update(
        id: int,
        specimen: SpecimenUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in specimen.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row