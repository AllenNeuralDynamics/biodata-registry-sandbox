"""
Auto-generated module to handle endpoint responses for
SchemaEntities
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.crud.core import SchemaEntityCreate, SchemaEntityUpdate, SchemaEntitiesPage, SchemaEntitiesFilter
from biodata_registry_api.models.core import SchemaEntities

from biodata_registry_api.session import get_session

from biodata_registry_api.routes import encode_next_token, decode_next_token
from fastapi_filter import FilterDepends

router = APIRouter()

@router.post(
    "/schema_entity",
    tags=["core"],
    response_model=SchemaEntities,
    operation_id="create_schema_entity"
)
async def create_schema_entity(
        schema_entity: SchemaEntityCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = SchemaEntities.model_validate(schema_entity.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/schema_entity",
    tags=["core"],
    response_model=SchemaEntities,
    operation_id="get_schema_entity"
)
async def get_schema_entity(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SchemaEntities, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/schema_entities",
    tags=["core"],
    response_model=SchemaEntitiesPage,
    operation_id="get_schema_entities"
)
async def get_schema_entities(
        next_token: str | None = Query(default=None),
        limit: int = Query(default=10, le=100, ge=1),
        filter_query: SchemaEntitiesFilter = FilterDepends(SchemaEntitiesFilter),
        session: AsyncSession = Depends(get_session),
):
    previous_id = decode_next_token(next_token)
    statement = select(SchemaEntities).order_by(SchemaEntities.id.asc())
    statement = filter_query.filter(statement)
    if previous_id is not None:
        statement = statement.where(SchemaEntities.id > previous_id)
    statement = statement.limit(limit)
    rows = await session.exec(statement)
    items = rows.all()
    next_token = None if not items else encode_next_token(items[-1].id)
    return SchemaEntitiesPage(
        next_token=next_token,
        has_more=len(items) == limit,
        results=items
    )

@router.delete(
    "/schema_entity",
    tags=["core"],
    operation_id="delete_schema_entity"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SchemaEntities, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/schema_entity",
    tags=["core"],
    response_model=SchemaEntities,
    operation_id="update_schema_entity"
)
async def update(
        id: int,
        schema_entity: SchemaEntityUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(SchemaEntities, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in schema_entity.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row