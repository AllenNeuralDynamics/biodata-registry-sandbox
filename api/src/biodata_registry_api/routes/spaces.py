"""
Auto-generated module to handle endpoint responses for
Spaces
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.crud.admin import SpaceCreate, SpaceUpdate, SpacesPage, SpacesFilter
from biodata_registry_api.models.admin import Spaces

from biodata_registry_api.session import get_session
from biodata_registry_api.routes import encode_next_token, decode_next_token
from fastapi_filter import FilterDepends

router = APIRouter()

@router.post(
    "/space",
    tags=["admin"],
    response_model=Spaces,
    operation_id="create_space"
)
async def create_space(
        space: SpaceCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Spaces.model_validate(space.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/space",
    tags=["admin"],
    response_model=Spaces,
    operation_id="get_space"
)
async def get_space(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Spaces, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/spaces",
    tags=["admin"],
    response_model=SpacesPage,
    operation_id="get_spaces"
)
async def get_spaces(
        next_token: str | None = Query(default=None),
        limit: int = Query(default=10, le=100, ge=1),
        filter_query: SpacesFilter = FilterDepends(SpacesFilter),
        session: AsyncSession = Depends(get_session),
):
    previous_id = decode_next_token(next_token)
    statement = select(Spaces).order_by(Spaces.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(Spaces.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return SpacesPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

@router.delete(
    "/space",
    tags=["admin"],
    operation_id="delete_space"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Spaces, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/space",
    tags=["admin"],
    response_model=Spaces,
    operation_id="update_space"
)
async def update(
        id: int,
        space: SpaceUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Spaces, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in space.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row