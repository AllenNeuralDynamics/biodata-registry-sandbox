"""
Auto-generated module to handle endpoint responses for
QualityControls
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import QualityControls, QualityControlCreate, QualityControlUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post("/quality_control", tags=["quality_controls"], response_model=QualityControls)
async def create_quality_control(
        quality_control: QualityControlCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = QualityControls.model_validate(quality_control.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get("/quality_control", tags=["quality_controls"], response_model=QualityControls)
async def get_quality_control(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(QualityControls, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get("/quality_controls", tags=["quality_controls"], response_model=List[QualityControls])
async def get_quality_controls(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(QualityControls).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete("/quality_control", tags=["quality_controls"])
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(QualityControls, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put("/quality_control", tags=["quality_controls"], response_model=QualityControls)
async def update(
        id: int,
        quality_control: QualityControlUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(QualityControls, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in quality_control.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row