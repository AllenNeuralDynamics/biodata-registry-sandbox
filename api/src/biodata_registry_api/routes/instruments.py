"""
Auto-generated module to handle endpoint responses for
Instruments
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Instruments, InstrumentCreate, InstrumentUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/instrument",
    tags=["core"],
    response_model=Instruments,
    operation_id="create_instrument"
)
async def create_instrument(
        instrument: InstrumentCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Instruments.model_validate(instrument.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/instrument",
    tags=["core"],
    response_model=Instruments,
    operation_id="get_instrument"
)
async def get_instrument(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Instruments, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/instruments",
    tags=["core"],
    response_model=List[Instruments],
    operation_id="get_instruments"
)
async def get_instruments(
        name: str | None = Query(default=None),
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    statement = select(Instruments).offset(offset).limit(limit)
    if name is not None:
        statement = statement.where(Instruments.name == name)
    rows = await session.exec(statement)
    return rows.all()

@router.delete(
    "/instrument",
    tags=["core"],
    operation_id="delete_instrument"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Instruments, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/instrument",
    tags=["core"],
    response_model=Instruments,
    operation_id="update_instrument"
)
async def update(
        id: int,
        instrument: InstrumentUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Instruments, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in instrument.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row
