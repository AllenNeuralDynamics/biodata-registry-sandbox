"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/acquisition_specimens", tags=["acquisition_specimens"])
async def get_acquisition_specimens(
    acquisition_id: Optional[int] = Query(
        None,
        alias="acquisition_id",
    ),
    specimen_id: Optional[int] = Query(
        None,
        alias="specimen_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [acquisition_id, specimen_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM acquisition_specimens"
    or_statement = ""
    param_dict = dict()
    if acquisition_id is not None:
        or_statement = " WHERE acquisition_id = :acquisition_id"
        param_dict["acquisition_id"] = acquisition_id
    if specimen_id is not None and not param_dict:
        or_statement = " WHERE specimen_id = :specimen_id"
        param_dict["specimen_id"] = specimen_id
    elif specimen_id is not None:
        or_statement = or_statement + " OR specimen_id = :specimen_id"
        param_dict["specimen_id"] = specimen_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"acquisition_id": row.acquisition_id, "specimen_id": row.specimen_id})
    return rows

@router.post("/acquisition_specimens", tags=["acquisition_specimens"])
async def create_acquisition_specimens(
    acquisition_id: int = Query(
        alias="acquisition_id",
    ),
    specimen_id: int = Query(
        alias="specimen_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO acquisition_specimens (acquisition_id, specimen_id) VALUES (:acquisition_id, :specimen_id) RETURNING *;"
    param_dict = {"acquisition_id": acquisition_id, "specimen_id": specimen_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"acquisition_id": row.acquisition_id, "specimen_id": row.specimen_id})
    return rows

@router.delete("/acquisition_specimens", tags=["acquisition_specimens"])
async def delete_acquisition_specimens(
    acquisition_id: int = Query(
        alias="acquisition_id",
    ),
    specimen_id: int = Query(
        alias="specimen_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM acquisition_specimens WHERE acquisition_id = :space_admin_id AND specimen_id = :specimen_id RETURNING *;"
    param_dict = {"acquisition_id": acquisition_id, "specimen_id": specimen_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"acquisition_id": row.acquisition_id, "specimen_id": row.specimen_id})
    return rows
