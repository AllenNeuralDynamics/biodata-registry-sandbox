"""
Auto-generated module to handle endpoint responses for
Acquisitions
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Acquisitions, AcquisitionCreate, AcquisitionUpdate, Subjects

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/acquisition",
    tags=["core"],
    response_model=Acquisitions,
    operation_id="create_acquisition"
)
async def create_acquisition(
        acquisition: AcquisitionCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Acquisitions.model_validate(acquisition.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/acquisition",
    tags=["core"],
    response_model=Acquisitions,
    operation_id="get_acquisition"
)
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

@router.get(
    "/acquisitions",
    tags=["core"],
    response_model=List[Acquisitions],
    operation_id="get_acquisitions"
)
async def get_acquisitions(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Acquisitions).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete(
    "/acquisition",
    tags=["core"],
    operation_id="delete_acquisition"
)
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

@router.put(
    "/acquisition",
    tags=["core"],
    response_model=Acquisitions,
    operation_id="update_acquisition"
)
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

@router.get(
    "/acquisition_subjects",
    tags=["core"],
    response_model=List[Subjects],
    operation_id="get_acquisition_subjects"
)
async def get_acquisition_subjects(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Acquisitions, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    subjects = row.subjects
    return subjects

@router.delete(
    "/acquisition_subject",
    tags=["core"],
    operation_id="remove_acquisition_subject"
)
async def remove_acquisition_subject(
        id: int,
        subject_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Acquisitions, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Subjects, subject_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{subject_id} not found!"
        )
    row.subjects.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Removed subject {subject_id} from acquisition {id}"
    }

@router.put(
    "/acquisition_subject",
    tags=["core"],
    operation_id="put_acquisition_subject"
)
async def add_acquisition_subject(
        id: int,
        subject_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Acquisitions, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Subjects, subject_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{subject_id} not found!"
        )
    row.subjects.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Added subject {subject_id} to acquisition {id}"
    }
