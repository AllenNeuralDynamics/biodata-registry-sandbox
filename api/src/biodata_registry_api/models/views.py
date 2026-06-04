from sqlmodel import SQLModel, Field, Column
from typing import Dict, Any, List
from sqlalchemy.dialects.postgresql import JSONB, JSON
from datetime import datetime


data_asset_view_statement = """
CREATE VIEW data_asset_view
AS SELECT
    data_assets.id AS data_asset_id,
    data_assets.created_at AS created_at,
    data_assets.updated_at AS updated_at,
    data_assets.created_by AS created_by,
    data_assets.updated_by AS updated_by,
    acquisitions.id AS acquisition_id,
    instruments.id AS instrument_id,
    processes.id AS process_id,
    data_assets.name AS data_asset_name,
    data_assets.location AS data_asset_location,
    data_assets.external_links AS data_asset_external_links,
    instruments.name AS instrument_name,
    data_assets.data AS data_asset_data,
    acquisitions.data AS acquisition_data,
    processes.data AS processes_data,
    instruments.data AS instrument_data,
    agg1.items as quality_control_metrics,
    agg2.items as subjects,
    agg3.items as subject_procedures
FROM data_assets
LEFT OUTER JOIN acquisitions ON data_assets.id = acquisitions.data_asset_id
LEFT OUTER JOIN instruments ON instruments.id = acquisitions.instrument_id
LEFT OUTER JOIN processes ON data_assets.id = processes.output_data_asset_id
LEFT JOIN LATERAL (
    SELECT COALESCE(
        jsonb_agg(jsonb_build_object(
            'quality_control_id', quality_controls.id, 
            'data', quality_controls.data
        )), '[]') as items
    FROM quality_controls
    WHERE quality_controls.data_asset_id = data_assets.id
) agg1 ON true
JOIN acquisition_subjects ON acquisitions.id = acquisition_subjects.acquisition_id
LEFT JOIN LATERAL (
    SELECT COALESCE(
        jsonb_agg(jsonb_build_object(
            'subject_id', subjects.id, 
            'data', subjects.data
        )), '[]') as items
    FROM subjects
    WHERE subjects.id = acquisition_subjects.subject_id
) agg2 ON true
LEFT JOIN LATERAL (
    SELECT COALESCE(
        jsonb_agg(jsonb_build_object(
            'subject_id', subject_procedures.subject_id, 
            'subject_procedures_id', subject_procedures.id,
            'data', subject_procedures.data
        )), '[]') as items
    FROM subject_procedures
    WHERE subject_procedures.subject_id = acquisition_subjects.subject_id
) agg3 ON true
;
"""

class DataAssetView(SQLModel, table=True):
    __tablename__ = "data_asset_view"

    created_at: datetime | None = Field(default=None)
    created_by: int | None = Field(default=None)
    updated_at: datetime | None = Field(default=None)
    updated_by: int | None = Field(default=None)
    data_asset_id: int | None = Field(
        default=None, primary_key=True
    )
    acquisition_id: int | None = Field(
        default=None, primary_key=True
    )
    process_id: int | None = Field(
        default=None, primary_key=True
    )
    instrument_id: int | None = Field(
        default=None, primary_key=True
    )
    acquisition_data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    processes_data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    instrument_name: str | None = Field(default=None, max_length=254)
    instrument_data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    data_asset_location: str | None = Field(default=None, max_length=254)
    data_asset_name: str | None = Field(default=None, max_length=254)
    data_asset_data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    data_asset_external_links: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    subjects: List[Dict[str, Any]] = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )
    subject_procedures: List[Dict[str, Any]] = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )
    quality_control_metrics: List[Dict[str, Any]] = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )
