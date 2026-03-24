"""
Auto-generated module to handle endpoint responses for
Processes
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Processes, ProcessCreate, ProcessUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post("/process", tags=["processes"], response_model=Processes)
async def create_process(
        process: ProcessCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Processes.model_validate(process.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get("/process", tags=["processes"], response_model=Processes)
async def get_process(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Processes, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get("/processes", tags=["processes"], response_model=List[Processes])
async def get_processes(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Processes).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete("/process", tags=["processes"])
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Processes, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put("/process", tags=["processes"], response_model=Processes)
async def update(
        id: int,
        process: ProcessUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Processes, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in process.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row