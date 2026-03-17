"""Module to handle endpoint responses"""
from typing import Optional

from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from aind_registry_service_api.session import get_session

router = APIRouter()

@router.get("/acquisition_subjects", tags=["acquisition_subjects"])
async def get_acquisition_subjects(
    acquisition_id: Optional[int] = Query(
        None,
        alias="acquisition_id",
    ),
    subject_id: Optional[int] = Query(
        None,
        alias="subject_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    if all(item is None for item in [acquisition_id, subject_id]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    base_statement = "SELECT * FROM acquisition_subjects"
    or_statement = ""
    param_dict = dict()
    if acquisition_id is not None:
        or_statement = " WHERE acquisition_id = :acquisition_id"
        param_dict["acquisition_id"] = acquisition_id
    if subject_id is not None and not param_dict:
        or_statement = " WHERE subject_id = :subject_id"
        param_dict["subject_id"] = subject_id
    elif subject_id is not None:
        or_statement = or_statement + " OR subject_id = :subject_id"
        param_dict["subject_id"] = subject_id
    new_statement = f"{base_statement} {or_statement};"
    statement = text(new_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"acquisition_id": row.acquisition_id, "subject_id": row.subject_id})
    return rows

@router.post("/acquisition_subjects", tags=["acquisition_subjects"])
async def create_acquisition_subjects(
    acquisition_id: int = Query(
        alias="acquisition_id",
    ),
    subject_id: int = Query(
        alias="subject_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "INSERT INTO acquisition_subjects (acquisition_id, subject_id) VALUES (:acquisition_id, :subject_id) RETURNING *;"
    param_dict = {"acquisition_id": acquisition_id, "subject_id": subject_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"acquisition_id": row.acquisition_id, "subject_id": row.subject_id})
    return rows

@router.delete("/acquisition_subjects", tags=["acquisition_subjects"])
async def delete_acquisition_subjects(
    acquisition_id: int = Query(
        alias="acquisition_id",
    ),
    subject_id: int = Query(
        alias="subject_id",
    ),
    session: AsyncSession = Depends(get_session),
):
    base_statement = "DELETE FROM acquisition_subjects WHERE acquisition_id = :space_admin_id AND subject_id = :subject_id RETURNING *;"
    param_dict = {"acquisition_id": acquisition_id, "subject_id": subject_id}
    statement = text(base_statement)
    result = await session.execute(statement, param_dict)
    rows = []
    for row in result:
        rows.append({"acquisition_id": row.acquisition_id, "subject_id": row.subject_id})
    return rows
