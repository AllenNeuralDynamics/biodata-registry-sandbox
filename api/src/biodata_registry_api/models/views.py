from sqlmodel import SQLModel, select, Field, Column
from sqlalchemy_utils.view import create_view
from typing import Dict, Any, List
from sqlalchemy.dialects.postgresql import JSONB, JSON
from biodata_registry_api.models.core import Acquisitions, DataAssets, Subjects, QualityControls, Instruments, Processes, SubjectProcedures
from biodata_registry_api.models.link_tables import AcquisitionSubjects


class DataAssetView(SQLModel, table=True):
    # __table__ = create_view(
    #     metadata=SQLModel.metadata,
    #     name="data_asset_view",
    #     selectable=select(
    #         DataAssets.id.label("data_asset_id"),
    #         Acquisitions.id.label("acquisition_id"),
    #         Subjects.id.label("subject_id"),
    #         Processes.id.label("process_id"),
    #         SubjectProcedures.id.label("subject_procedure_id"),
    #         QualityControls.id.label("quality_control_id"),
    #         Instruments.id.label("instrument_id"),
    #         Processes.data.label("processes_data"),
    #         Acquisitions.data.label("acquisition_data"),
    #         Instruments.name.label("instrument_name"),
    #         Instruments.data.label("instrument_data"),
    #         DataAssets.location.label("data_asset_location"),
    #         DataAssets.name.label("data_asset_name"),
    #         DataAssets.data.label("data_asset_data"),
    #         DataAssets.external_links.label("data_asset_external_links"),
    #         Subjects.name.label("subject_name"),
    #         Subjects.data.label("subject_data"),
    #         SubjectProcedures.data.label("subject_procedures_data"),
    #         QualityControls.data.label("quality_control_data")
    #     ).join(
    #         Acquisitions, DataAssets.id == Acquisitions.data_asset_id, isouter=True
    #     ).join(
    #         Instruments, Instruments.id == Acquisitions.instrument_id, isouter=True
    #     ).join(
    #         QualityControls, DataAssets.id == QualityControls.data_asset_id , isouter=True
    #     ).join(
    #         Processes, DataAssets.id == Processes.output_data_asset_id, isouter=True
    #     ).join(
    #         AcquisitionSubjects
    #     ).join(
    #         Subjects
    #     ).join(
    #         SubjectProcedures, SubjectProcedures.subject_id == Subjects.id, isouter=True
    #     )
    # )
    __tablename__ = "data_asset_view"
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
