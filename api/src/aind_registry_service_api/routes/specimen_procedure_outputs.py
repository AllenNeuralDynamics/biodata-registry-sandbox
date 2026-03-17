"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/specimen_procedure_outputs", tags=["specimen_procedure_outputs"])
async def get_specimen_procedure_outputs(
    specimen_id: Optional[int] = Query(
        None,
        alias="specimen_id",
    ),
    specimen_procedure_id: Optional[int] = Query(
        None,
        alias="specimen_procedure_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [specimen_id, specimen_procedure_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM specimen_procedure_outputs"
    or_statement = ""
    param_dict = dict()
    if specimen_id is not None:
        or_statement = " WHERE specimen_id = :specimen_id"
        param_dict["specimen_id"] = specimen_id
    if specimen_procedure_id is not None and not param_dict:
        or_statement = " WHERE specimen_procedure_id = :specimen_procedure_id"
        param_dict["specimen_procedure_id"] = specimen_procedure_id
    elif specimen_procedure_id is not None:
        or_statement = or_statement + " OR specimen_procedure_id = :specimen_procedure_id"
        param_dict["specimen_procedure_id"] = specimen_procedure_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"specimen_id": row.specimen_id, "specimen_procedure_id": row.specimen_procedure_id})
    return rows

@router.post("/specimen_procedure_outputs", tags=["specimen_procedure_outputs"])
async def create_specimen_procedure_outputs(
    specimen_id: int = Query(
        alias="specimen_id",
    ),
    specimen_procedure_id: int = Query(
        alias="specimen_procedure_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO specimen_procedure_outputs (specimen_id, specimen_procedure_id) VALUES (:specimen_id, :specimen_procedure_id) RETURNING *;"
    param_dict = {"specimen_id": specimen_id, "specimen_procedure_id": specimen_procedure_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"specimen_id": row.specimen_id, "specimen_procedure_id": row.specimen_procedure_id})
    return rows

@router.delete("/specimen_procedure_outputs", tags=["specimen_procedure_outputs"])
async def delete_specimen_procedure_outputs(
    specimen_id: int = Query(
        alias="specimen_id",
    ),
    specimen_procedure_id: int = Query(
        alias="specimen_procedure_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM specimen_procedure_outputs WHERE specimen_id = :space_admin_id AND specimen_procedure_id = :specimen_procedure_id RETURNING *;"
    param_dict = {"specimen_id": specimen_id, "specimen_procedure_id": specimen_procedure_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"specimen_id": row.specimen_id, "specimen_procedure_id": row.specimen_procedure_id})
    return rows
