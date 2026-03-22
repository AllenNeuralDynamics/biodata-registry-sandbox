"""
Auto-generated module to handle endpoint responses for
Schemas
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Schemas, SchemaCreate, SchemaUpdate

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post("/schema", tags=["schemas"], response_model=Schemas)
async def create_schema(
        schema: SchemaCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Schemas.model_validate(schema.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get("/schema", tags=["schemas"], response_model=Schemas)
async def get_schema(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Schemas, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get("/schemas", tags=["schemas"], response_model=List[Schemas])
async def get_schemas(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Schemas).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete("/schema", tags=["schemas"])
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Schemas, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put("/schema", tags=["schemas"], response_model=Schemas)
async def update(
        id: int,
        schema: SchemaUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Schemas, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in schema.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row