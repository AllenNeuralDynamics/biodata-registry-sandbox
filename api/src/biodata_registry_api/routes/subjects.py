"""
Auto-generated module to handle endpoint responses for
Subjects
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Subjects, SubjectCreate, SubjectUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post("/subject", tags=["subjects"], response_model=Subjects)
async def create_subject(
        subject: SubjectCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Subjects.model_validate(subject.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get("/subject", tags=["subjects"], response_model=Subjects)
async def get_subject(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Subjects, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get("/subjects", tags=["subjects"], response_model=List[Subjects])
async def get_subjects(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Subjects).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete("/subject", tags=["subjects"])
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Subjects, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put("/subject", tags=["subjects"], response_model=Subjects)
async def update(
        id: int,
        subject: SubjectUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Subjects, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in subject.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row