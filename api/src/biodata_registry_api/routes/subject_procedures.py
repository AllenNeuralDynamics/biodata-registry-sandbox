"""
Auto-generated module to handle endpoint responses for
SubjectProcedures
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.crud.core import SubjectProceduresFilter, SubjectProceduresPage, SubjectProcedureCreate, SubjectProcedureUpdate
from biodata_registry_api.models.core import SubjectProcedures, Specimens
from biodata_registry_api.routes import encode_next_token, decode_next_token

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
    response_model=SubjectProceduresPage,
    operation_id="get_subject_procedures"
)
async def get_subject_procedures(
        filter_query: SubjectProceduresFilter = Depends(),
        session: AsyncSession = Depends(get_session),
):
    next_token = filter_query.next_token
    limit = filter_query.limit
    previous_id = decode_next_token(next_token)
    statement = select(SubjectProcedures).order_by(SubjectProcedures.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(SubjectProcedures.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return SubjectProceduresPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

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
