"""
Auto-generated module to handle endpoint responses for
SubjectProcedures
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import SubjectProcedures, SubjectProcedureCreate, SubjectProcedureUpdate, \
    Specimens

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/subject_procedure",
    tags=["core"],
    response_model=SubjectProcedures,
    operation_id="create_subject_procedure"
)
async def create_subject_procedure(
        subject_procedure: SubjectProcedureCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = SubjectProcedures.model_validate(subject_procedure.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/subject_procedure",
    tags=["core"],
    response_model=SubjectProcedures,
    operation_id="get_subject_procedure"
)
async def get_subject_procedure(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SubjectProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/subject_procedures",
    tags=["core"],
    response_model=List[SubjectProcedures],
    operation_id="get_subject_procedures"
)
async def get_subject_procedures(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(SubjectProcedures).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete(
    "/subject_procedure",
    tags=["core"],
    operation_id="delete_subject_procedure"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SubjectProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/subject_procedure",
    tags=["core"],
    response_model=SubjectProcedures,
    operation_id="update_subject_procedure"
)
async def update(
        id: int,
        subject_procedure: SubjectProcedureUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SubjectProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in subject_procedure.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row

@router.get(
    "/subject_procedure_specimens",
    tags=["core"],
    response_model=List[Specimens],
    operation_id="get_subject_procedure_specimens"
)
async def get_subject_procedure_specimens(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SubjectProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    specimens = row.specimens
    return specimens

@router.delete(
    "/subject_procedure_specimen",
    tags=["core"],
    operation_id="remove_subject_procedure_specimen"
)
async def remove_subject_procedure_specimen(
        id: int,
        specimen_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SubjectProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Specimens, specimen_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_id} not found!"
        )
    row.specimens.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Removed specimen {specimen_id} from subject_procedure {id}"
    }

@router.put(
    "/subject_procedure_specimen",
    tags=["core"],
    operation_id="put_subject_procedure_specimen"
)
async def add_subject_procedure_specimen(
        id: int,
        specimen_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SubjectProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Specimens, specimen_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_id} not found!"
        )
    row.specimens.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Added specimen {specimen_id} to subject_procedure {id}"
    }
