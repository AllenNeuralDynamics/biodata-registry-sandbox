"""
Auto-generated module to handle endpoint responses for
SchemaEntities
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import SchemaEntities, SchemaEntityCreate, SchemaEntityUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post("/schema_entity", tags=["schema_entities"], response_model=SchemaEntities)
async def create_schema_entity(
        schema_entity: SchemaEntityCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = SchemaEntities.model_validate(schema_entity.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get("/schema_entity", tags=["schema_entities"], response_model=SchemaEntities)
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

@router.get("/schema_entities", tags=["schema_entities"], response_model=List[SchemaEntities])
async def get_schema_entities(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(SchemaEntities).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete("/schema_entity", tags=["schema_entities"])
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

@router.put("/schema_entity", tags=["schema_entities"], response_model=SchemaEntities)
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