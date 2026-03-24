"""
Auto-generated module to handle endpoint responses for
Acquisitions
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Acquisitions, AcquisitionCreate, AcquisitionUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post("/acquisition", tags=["acquisitions"], response_model=Acquisitions)
async def create_acquisition(
        acquisition: AcquisitionCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Acquisitions.model_validate(acquisition.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get("/acquisition", tags=["acquisitions"], response_model=Acquisitions)
async def get_acquisition(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Acquisitions, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get("/acquisitions", tags=["acquisitions"], response_model=List[Acquisitions])
async def get_acquisitions(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Acquisitions).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete("/acquisition", tags=["acquisitions"])
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Acquisitions, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put("/acquisition", tags=["acquisitions"], response_model=Acquisitions)
async def update(
        id: int,
        acquisition: AcquisitionUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Acquisitions, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in acquisition.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row