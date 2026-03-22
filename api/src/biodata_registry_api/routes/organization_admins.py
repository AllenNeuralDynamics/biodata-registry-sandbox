"""
Auto-generated module to handle endpoint responses for
OrganizationAdmins
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.admin import OrganizationAdmins, OrganizationAdminCreate, OrganizationAdminUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post("/organization_admin", tags=["organization_admins"], response_model=OrganizationAdmins)
async def create_organization_admin(
        organization_admin: OrganizationAdminCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = OrganizationAdmins.model_validate(organization_admin.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get("/organization_admin", tags=["organization_admins"], response_model=OrganizationAdmins)
async def get_organization_admin(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(OrganizationAdmins, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get("/organization_admins", tags=["organization_admins"], response_model=List[OrganizationAdmins])
async def get_organization_admins(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(OrganizationAdmins).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete("/organization_admin", tags=["organization_admins"])
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(OrganizationAdmins, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put("/organization_admin", tags=["organization_admins"], response_model=OrganizationAdmins)
async def update(
        id: int,
        organization_admin: OrganizationAdminUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(OrganizationAdmins, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in organization_admin.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row