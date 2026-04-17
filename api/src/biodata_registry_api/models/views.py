from sqlmodel import SQLModel, select, Field, Column
from sqlalchemy_utils.view import create_view
from typing import Dict, Any
from sqlalchemy.dialects.postgresql import JSONB
from biodata_registry_api.models.core import Acquisitions, DataAssets, Subjects, QualityControls, Instruments
from biodata_registry_api.models.link_tables import AcquisitionSubjects


class AcquisitionView(SQLModel, table=True):
    # __table__ = create_view(
    #     metadata=SQLModel.metadata,
    #     name="acquisition_view",
    #     selectable=select(
    #         Acquisitions.id.label("acquisition_id"),
    #         Subjects.id.label("subject_id"),
    #         Acquisitions.data.label("acquisition_data"),
    #         Instruments.name.label("instrument_name"),
    #         Instruments.data.label("instrument_data"),
    #         DataAssets.location.label("data_asset_location"),
    #         DataAssets.name.label("data_asset_name"),
    #         DataAssets.data.label("data_asset_data"),
    #         DataAssets.external_links.label("data_asset_external_links"),
    #         Subjects.name.label("subject_name"),
    #         Subjects.data.label("subject_data"),
    #         QualityControls.data.label("quality_control_data")
    #     ).join(
    #         DataAssets, DataAssets.id == Acquisitions.data_asset_id, isouter=True
    #     ).join(
    #         Instruments, Instruments.id == Acquisitions.instrument_id, isouter=True
    #     ).join(
    #         QualityControls, QualityControls.data_asset_id == Acquisitions.data_asset_id, isouter=True
    #     ).join(
    #         AcquisitionSubjects
    #     ).join(
    #         Subjects
    #     )
    # )
    __tablename__ = "acquisition_view"
    acquisition_id: int | None = Field(
        default=None, primary_key=True
    )
    subject_id: int | None = Field(
        default=None, primary_key=True
    )
    acquisition_data: Dict[str, Any] = Field(
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
    subject_name: str | None = Field(default=None, max_length=254)
    subject_data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    quality_control_data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )

class DataAssetView(SQLModel, table=True):
    # __table__ = create_view(
    #     metadata=SQLModel.metadata,
    #     name="data_asset_view",
    #     selectable=select(
    #         DataAssets.id.label("data_asset_id"),
    #         Acquisitions.id.label("acquisition_id"),
    #         Subjects.id.label("subject_id"),
    #         Acquisitions.data.label("acquisition_data"),
    #         Instruments.name.label("instrument_name"),
    #         Instruments.data.label("instrument_data"),
    #         DataAssets.location.label("data_asset_location"),
    #         DataAssets.name.label("data_asset_name"),
    #         DataAssets.data.label("data_asset_data"),
    #         DataAssets.external_links.label("data_asset_external_links"),
    #         Subjects.name.label("subject_name"),
    #         Subjects.data.label("subject_data"),
    #         QualityControls.data.label("quality_control_data")
    #     ).join(
    #         Acquisitions, DataAssets.id == Acquisitions.data_asset_id, isouter=True
    #     ).join(
    #         Instruments, Instruments.id == Acquisitions.instrument_id, isouter=True
    #     ).join(
    #         QualityControls, QualityControls.data_asset_id == Acquisitions.data_asset_id, isouter=True
    #     ).join(
    #         AcquisitionSubjects
    #     ).join(
    #         Subjects
    #     )
    # )
    __tablename__ = "data_asset_view"
    data_asset_id: int | None = Field(
        default=None, primary_key=True
    )
    acquisition_id: int | None = Field(
        default=None, primary_key=True
    )
    subject_id: int | None = Field(
        default=None, primary_key=True
    )
    acquisition_data: Dict[str, Any] = Field(
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
    subject_name: str | None = Field(default=None, max_length=254)
    subject_data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    quality_control_data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
