"""
Auto-generated module to handle endpoint responses for
OrganizationAdmins
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.crud.admin import OrganizationAdminsPage, OrganizationAdminsFilter, OrganizationAdminCreate, OrganizationAdminUpdate
from biodata_registry_api.models.admin import OrganizationAdmins

from biodata_registry_api.session import get_session
from biodata_registry_api.routes import encode_next_token, decode_next_token
from fastapi_filter import FilterDepends

router = APIRouter()

@router.post(
    "/organization_admin",
    tags=["admin"],
    response_model=OrganizationAdmins,
    operation_id="create_organization_admin"
)
async def create_organization_admin(
        organization_admin: OrganizationAdminCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = OrganizationAdmins.model_validate(organization_admin.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/organization_admin",
    tags=["admin"],
    response_model=OrganizationAdmins,
    operation_id="get_organization_admin"
)
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

@router.get(
    "/organization_admins",
    tags=["admin"],
    response_model=OrganizationAdminsPage,
    operation_id="get_organization_admins"
)
async def get_organization_admins(
        next_token: str | None = Query(default=None),
        limit: int = Query(default=10, le=100, ge=1),
        filter_query: OrganizationAdminsFilter = FilterDepends(OrganizationAdminsFilter),
        session: AsyncSession = Depends(get_session),
):
    previous_id = decode_next_token(next_token)
    statement = select(OrganizationAdmins).order_by(OrganizationAdmins.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(OrganizationAdmins.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return OrganizationAdminsPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

@router.delete(
    "/organization_admin",
    tags=["admin"],
    operation_id="delete_organization_admin"
)
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

@router.put(
    "/organization_admin",
    tags=["admin"],
    response_model=OrganizationAdmins,
    operation_id="update_organization_admin"
)
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