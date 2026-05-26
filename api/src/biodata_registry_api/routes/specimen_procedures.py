"""
Auto-generated module to handle endpoint responses for
SpecimenProcedures
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.crud.core import SpecimenProcedureCreate, SpecimenProcedureUpdate, SpecimenProceduresFilter, SpecimenProceduresPage
from biodata_registry_api.models.core import SpecimenProcedures, Specimens
from biodata_registry_api.routes import encode_next_token, decode_next_token

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
    response_model=SpecimenProceduresPage,
    operation_id="get_specimen_procedures"
)
async def get_specimen_procedures(
        filter_query: SpecimenProceduresFilter = Depends(),
        session: AsyncSession = Depends(get_session),
):
    next_token = filter_query.next_token
    limit = filter_query.limit
    previous_id = decode_next_token(next_token)
    statement = select(SpecimenProcedures).order_by(SpecimenProcedures.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(SpecimenProcedures.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return SpecimenProceduresPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

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

@router.get(
    "/specimen_procedure_specimen_inputs",
    tags=["core"],
    response_model=List[Specimens],
    operation_id="get_specimen_procedure_specimen_inputs"
)
async def get_specimen_procedure_specimen_inputs(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpecimenProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    specimen_inputs = row.specimen_inputs
    return specimen_inputs

@router.delete(
    "/specimen_procedure_specimen_input",
    tags=["core"],
    operation_id="remove_specimen_procedure_specimen_input"
)
async def remove_specimen_procedure_specimen_input(
        id: int,
        specimen_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpecimenProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Specimens, specimen_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_id} not found!"
        )
    row.specimen_inputs.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": (
            f"Removed specimen_input {specimen_id} from specimen_procedure"
            f" {id}"
        )
    }

@router.put(
    "/specimen_procedure_specimen_input",
    tags=["core"],
    operation_id="put_specimen_procedure_specimen_input"
)
async def add_specimen_procedure_specimen_input(
        id: int,
        specimen_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpecimenProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Specimens, specimen_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_id} not found!"
        )
    row.specimen_inputs.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Added specimen_input {specimen_id} to specimen_procedure {id}"
    }

@router.get(
    "/specimen_procedure_specimen_outputs",
    tags=["core"],
    response_model=List[Specimens],
    operation_id="get_specimen_procedure_specimen_outputs"
)
async def get_specimen_procedure_specimen_outputs(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpecimenProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    specimen_outputs = row.specimen_outputs
    return specimen_outputs

@router.delete(
    "/specimen_procedure_specimen_output",
    tags=["core"],
    operation_id="remove_specimen_procedure_specimen_output"
)
async def remove_specimen_procedure_specimen_output(
        id: int,
        specimen_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpecimenProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Specimens, specimen_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_id} not found!"
        )
    row.specimen_outputs.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": (
            f"Removed specimen_output {specimen_id} from specimen_procedure"
            f" {id}"
        )
    }

@router.put(
    "/specimen_procedure_specimen_output",
    tags=["core"],
    operation_id="put_specimen_procedure_specimen_output"
)
async def add_specimen_procedure_specimen_output(
        id: int,
        specimen_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SpecimenProcedures, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Specimens, specimen_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_id} not found!"
        )
    row.specimen_outputs.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": (
            f"Added specimen_output {specimen_id} to specimen_procedure {id}"
        )
    }
