"""
Auto-generated module to handle endpoint responses for
SpecimenProcedures
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import SpecimenProcedures, SpecimenProcedureCreate, SpecimenProcedureUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/specimen_procedure",
    tags=["core"],
    response_model=SpecimenProcedures,
    operation_id="create_specimen_procedure"
)
async def create_specimen_procedure(
        specimen_procedure: SpecimenProcedureCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = SpecimenProcedures.model_validate(specimen_procedure.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/specimen_procedure",
    tags=["core"],
    response_model=SpecimenProcedures,
    operation_id="get_specimen_procedure"
)
async def get_specimen_procedure(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpecimenProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/specimen_procedures",
    tags=["core"],
    response_model=List[SpecimenProcedures],
    operation_id="get_specimen_procedures"
)
async def get_specimen_procedures(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(SpecimenProcedures).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete(
    "/specimen_procedure",
    tags=["core"],
    operation_id="delete_specimen_procedure"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpecimenProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/specimen_procedure",
    tags=["core"],
    response_model=SpecimenProcedures,
    operation_id="update_specimen_procedure"
)
async def update(
        id: int,
        specimen_procedure: SpecimenProcedureUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpecimenProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in specimen_procedure.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row