"""
Auto-generated module to handle endpoint responses for
Processes
"""
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from biodata_registry_api.models.core import Processes, ProcessCreate, ProcessUpdate, DataAssets

from biodata_registry_api.session import get_session

router = APIRouter()

@router.post(
    "/process",
    tags=["core"],
    response_model=Processes,
    operation_id="create_process"
)
async def create_process(
        process: ProcessCreate,
        session: AsyncSession = Depends(get_session),
):
    db_row = Processes.model_validate(process.model_dump())
    session.add(db_row)
    await session.commit()
    await session.refresh(db_row)
    return db_row

@router.get(
    "/process",
    tags=["core"],
    response_model=Processes,
    operation_id="get_process"
)
async def get_process(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Processes, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    return row

@router.get(
    "/processes",
    tags=["core"],
    response_model=List[Processes],
    operation_id="get_processes"
)
async def get_processes(
        offset: int = Query(default=0),
        limit: int = Query(default=10, le=1000),
        session: AsyncSession = Depends(get_session),
):
    rows = await session.exec(
        select(Processes).offset(offset).limit(limit)
    )
    return rows.all()

@router.delete(
    "/process",
    tags=["core"],
    operation_id="delete_process"
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Processes, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    await session.delete(row)
    await session.commit()
    return {"ok": True, "msg": f"Deleted {id}"}

@router.put(
    "/process",
    tags=["core"],
    response_model=Processes,
    operation_id="update_process"
)
async def update(
        id: int,
        process: ProcessUpdate,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Processes, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    for k, v in process.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row

@router.get(
    "/process_data_asset_inputs",
    tags=["core"],
    response_model=List[DataAssets],
    operation_id="get_process_data_asset_inputs"
)
async def get_process_data_asset_inputs(
        id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Processes, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    data_assets = row.data_asset_inputs
    return data_assets

@router.delete(
    "/process_data_asset_input",
    tags=["core"],
    operation_id="remove_process_data_asset_input"
)
async def remove_process_data_asset_input(
        id: int,
        data_asset_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Processes, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(DataAssets, data_asset_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{data_asset_id} not found!"
        )
    row.data_asset_inputs.remove(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Removed data_asset {data_asset_id} from process {id}"
    }

@router.put(
    "/process_data_asset_input",
    tags=["core"],
    operation_id="put_process_data_asset_input"
)
async def add_process_data_asset_input(
        id: int,
        data_asset_id: int,
        session: AsyncSession = Depends(get_session),
):
    row = await session.get(Processes, id)
    if not row:
        raise HTTPException(
            status_code=404, detail=f"{id} not found!"
        )
    foreign_row = await session.get(DataAssets, data_asset_id)
    if not foreign_row:
        raise HTTPException(
            status_code=404, detail=f"{data_asset_id} not found!"
        )
    row.data_asset_inputs.add(foreign_row)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return {
        "ok": True,
        "msg": f"Added data_asset {data_asset_id} to process {id}"
    }
