"""
Auto-generated module to handle endpoint responses for
QualityControls
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.crud.core import QualityControlCreate, QualityControlUpdate, QualityControlsFilter, QualityControlsPage
from biodata_registry_api.models.core import QualityControls

from biodata_registry_api.session import get_session
from biodata_registry_api.routes import encode_next_token, decode_next_token
from fastapi_filter import FilterDepends

router = APIRouter()

@router.post(
    "/quality_control",
    tags=["core"],
    response_model=QualityControls,
    operation_id="create_quality_control"
)
async def create_quality_control(
        quality_control: QualityControlCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = QualityControls.model_validate(quality_control.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/quality_control",
    tags=["core"],
    response_model=QualityControls,
    operation_id="get_quality_control"
)
async def get_quality_control(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(QualityControls, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/quality_controls",
    tags=["core"],
    response_model=QualityControlsPage,
    operation_id="get_quality_controls"
)
async def get_quality_controls(
        next_token: str | None = Query(default=None),
        limit: int = Query(default=10, le=100, ge=1),
        filter_query: QualityControlsFilter = FilterDepends(QualityControlsFilter),
        session: AsyncSession = Depends(get_session),
):
    previous_id = decode_next_token(next_token)
    statement = select(QualityControls).order_by(QualityControls.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(QualityControls.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return QualityControlsPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

@router.delete(
    "/quality_control",
    tags=["core"],
    operation_id="delete_quality_control"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(QualityControls, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/quality_control",
    tags=["core"],
    response_model=QualityControls,
    operation_id="update_quality_control"
)
async def update(
        id: int,
        quality_control: QualityControlUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(QualityControls, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in quality_control.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row