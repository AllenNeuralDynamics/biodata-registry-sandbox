"""
Auto-generated module to handle endpoint responses for
Specimens
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Specimens, SpecimenCreate, SpecimenUpdate, Acquisitions, SubjectProcedures, \
    SpecimenProcedures

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/specimen",
    tags=["core"],
    response_model=Specimens,
    operation_id="create_specimen"
)
async def create_specimen(
        specimen: SpecimenCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Specimens.model_validate(specimen.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/specimen",
    tags=["core"],
    response_model=Specimens,
    operation_id="get_specimen"
)
async def get_specimen(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/specimens",
    tags=["core"],
    response_model=List[Specimens],
    operation_id="get_specimens"
)
async def get_specimens(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Specimens).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete(
    "/specimen",
    tags=["core"],
    operation_id="delete_specimen"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/specimen",
    tags=["core"],
    response_model=Specimens,
    operation_id="update_specimen"
)
async def update(
        id: int,
        specimen: SpecimenUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in specimen.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row

@router.get(
    "/specimen_acquisitions",
    tags=["core"],
    response_model=List[Acquisitions],
    operation_id="get_specimen_acquisitions"
)
async def get_specimen_acquisitions(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    acquisitions = row.acquisitions
    return acquisitions

@router.delete(
    "/specimen_acquisition",
    tags=["core"],
    operation_id="remove_specimen_acquisition"
)
async def remove_specimen_acquisition(
        id: int,
        acquisition_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
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
        "msg": f"Removed acquisition {acquisition_id} from specimen {id}"
    }

@router.put(
    "/specimen_acquisition",
    tags=["core"],
    operation_id="put_specimen_acquisition"
)
async def add_specimen_acquisition(
        id: int,
        acquisition_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(Acquisitions, acquisition_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{acquisition_id} not found!"
        )
    row.specimens.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Added acquisition {acquisition_id} to specimen {id}"
    }

@router.get(
    "/specimen_subject_procedures",
    tags=["core"],
    response_model=List[SubjectProcedures],
    operation_id="get_specimen_subject_procedures"
)
async def get_specimen_subject_procedures(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    subject_procedures = row.subject_procedures
    return subject_procedures

@router.delete(
    "/specimen_subject_procedure",
    tags=["core"],
    operation_id="remove_specimen_subject_procedure"
)
async def remove_specimen_subject_procedure(
        id: int,
        subject_procedure_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(SubjectProcedures, subject_procedure_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{subject_procedure_id} not found!"
        )
    row.subject_procedures.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": (
            f"Removed subject_procedure {subject_procedure_id} from specimen"
            f" {id}"
        )
    }

@router.put(
    "/specimen_subject_procedure",
    tags=["core"],
    operation_id="put_specimen_subject_procedure"
)
async def add_specimen_subject_procedure(
        id: int,
        subject_procedure_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(SubjectProcedures, subject_procedure_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{subject_procedure_id} not found!"
        )
    row.subject_procedures.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": (
            f"Added subject_procedure {subject_procedure_id} to specimen {id}"
        )
    }

@router.get(
    "/specimen_specimen_procedure_inputs",
    tags=["core"],
    response_model=List[SpecimenProcedures],
    operation_id="get_specimen_specimen_procedure_inputs"
)
async def get_specimen_specimen_procedure_inputs(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    specimen_procedures_inputs = row.specimen_procedures_inputs
    return specimen_procedures_inputs

@router.delete(
    "/specimen_specimen_procedure_input",
    tags=["core"],
    operation_id="remove_specimen_specimen_procedure_input"
)
async def remove_specimen_specimen_procedure_input(
        id: int,
        specimen_procedure_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(SpecimenProcedures, specimen_procedure_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_procedure_id} not found!"
        )
    row.specimen_procedures_inputs.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": (
            f"Removed specimen_procedure_input {specimen_procedure_id} from "
            f"specimen {id}"
        )
    }

@router.put(
    "/specimen_specimen_procedure_input",
    tags=["core"],
    operation_id="put_specimen_specimen_procedure_input"
)
async def add_specimen_specimen_procedure_input(
        id: int,
        specimen_procedure_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(SpecimenProcedures, specimen_procedure_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_procedure_id} not found!"
        )
    row.specimen_procedures_inputs.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": (
            f"Added specimen_procedure_input {specimen_procedure_id} to"
            f" specimen {id}"
        )
    }

@router.get(
    "/specimen_specimen_procedure_outputs",
    tags=["core"],
    response_model=List[SpecimenProcedures],
    operation_id="get_specimen_specimen_procedure_outputs"
)
async def get_specimen_specimen_procedure_outputs(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    specimen_procedures_outputs = row.specimen_procedures_outputs
    return specimen_procedures_outputs

@router.delete(
    "/specimen_specimen_procedure_output",
    tags=["core"],
    operation_id="remove_specimen_specimen_procedure_output"
)
async def remove_specimen_specimen_procedure_output(
        id: int,
        specimen_procedure_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(SpecimenProcedures, specimen_procedure_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_procedure_id} not found!"
        )
    row.specimen_procedures_outputs.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": (
            f"Removed specimen_procedure_output {specimen_procedure_id} from "
            f"specimen {id}"
        )
    }

@router.put(
    "/specimen_specimen_procedure_output",
    tags=["core"],
    operation_id="put_specimen_specimen_procedure_output"
)
async def add_specimen_specimen_procedure_output(
        id: int,
        specimen_procedure_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Specimens, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(SpecimenProcedures, specimen_procedure_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{specimen_procedure_id} not found!"
        )
    row.specimen_procedures_outputs.append(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": (
            f"Added specimen_procedure_output {specimen_procedure_id} to"
            f" specimen {id}"
        )
    }
