"""
Auto-generated module to handle endpoint responses for
Subjects
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Subjects, Acquisitions
from biodata_registry_api.models.crud.core import SubjectCreate, SubjectUpdate, SubjectsPage, SubjectsFilter
from biodata_registry_api.session import get_session
from biodata_registry_api.routes import encode_next_token, decode_next_token
from fastapi_filter import FilterDepends

router = APIRouter()

@router.post(
    "/subject",
    tags=["core"],
    response_model=Subjects,
    operation_id="create_subject"
)
async def create_subject(
        subject: SubjectCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Subjects.model_validate(subject.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/subject",
    tags=["core"],
    response_model=Subjects,
    operation_id="get_subject"
)
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

@router.get(
    "/subjects",
    tags=["core"],
    response_model=SubjectsPage,
    operation_id="get_subjects"
)
async def get_subjects(
        next_token: str | None = Query(default=None),
        limit: int = Query(default=10, le=100, ge=1),
        filter_query: SubjectsFilter = FilterDepends(SubjectsFilter),
        session: AsyncSession = Depends(get_session),
):
    previous_id = decode_next_token(next_token)
    statement = select(Subjects).order_by(Subjects.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(Subjects.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return SubjectsPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

@router.delete(
    "/subject",
    tags=["core"],
    operation_id="delete_subject"
)
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

@router.put(
    "/subject",
    tags=["core"],
    response_model=Subjects,
    operation_id="update_subject"
)
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

@router.get(
    "/subject_acquisitions",
    tags=["core"],
    response_model=List[Acquisitions],
    operation_id="get_subject_acquisitions"
)
async def get_subject_acquisitions(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Subjects, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    acquisitions = row.acquisitions
    return acquisitions

@router.delete(
    "/subject_acquisition",
    tags=["core"],
    operation_id="remove_subject_acquisition"
)
async def remove_subject_acquisition(
        id: int,
        acquisition_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Subjects, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Acquisitions, acquisition_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{acquisition_id} not found!"
        )
    row.acquisitions.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Removed acquisition {acquisition_id} from subject {id}"
    }

@router.put(
    "/subject_acquisition",
    tags=["core"],
    operation_id="put_subject_acquisition"
)
async def add_subject_acquisition(
        id: int,
        acquisition_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Subjects, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Acquisitions, acquisition_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{acquisition_id} not found!"
        )
    row.acquisitions.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Added acquisition {acquisition_id} to subject {id}"
    }
