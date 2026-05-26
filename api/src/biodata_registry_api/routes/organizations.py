"""
Auto-generated module to handle endpoint responses for
Organizations
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.crud.admin import OrganizationCreate, OrganizationUpdate, OrganizationsPage, OrganizationsFilter
from biodata_registry_api.models.admin import Organizations

from biodata_registry_api.session import get_session
from biodata_registry_api.routes import encode_next_token, decode_next_token

router = APIRouter()

@router.post(
    "/organization",
    tags=["admin"],
    response_model=Organizations,
    operation_id="create_organization"
)
async def create_organization(
        organization: OrganizationCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Organizations.model_validate(organization.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/organization",
    tags=["admin"],
    response_model=Organizations,
    operation_id="get_organization"
)
async def get_organization(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Organizations, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/organizations",
    tags=["admin"],
    response_model=OrganizationsPage,
    operation_id="get_organizations"
)
async def get_organizations(
        filter_query: OrganizationsFilter = Depends(),
        session: AsyncSession = Depends(get_session),
):
    next_token = filter_query.next_token
    limit = filter_query.limit
    previous_id = decode_next_token(next_token)
    statement = select(Organizations).order_by(Organizations.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(Organizations.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return OrganizationsPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

@router.delete(
    "/organization",
    tags=["admin"],
    operation_id="delete_organization"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Organizations, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/organization",
    tags=["admin"],
    response_model=Organizations,
    operation_id="update_organization"
)
async def update(
        id: int,
        organization: OrganizationUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Organizations, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in organization.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row