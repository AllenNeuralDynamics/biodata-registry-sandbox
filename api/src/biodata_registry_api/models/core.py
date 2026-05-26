from biodata_registry_api.models.link_tables import (
    CollectionDataAssets,
    AcquisitionSubjects,
    ProcessInputs,
    SpecimenProcedureInputs,
    SpecimenProcedureOutputs,
    SubjectProcedureOutputs,
    AcquisitionSpecimens
)
from sqlmodel import Field, Column, Relationship, UniqueConstraint
from typing import Dict, Any, List
from sqlalchemy.dialects.postgresql import JSONB
from biodata_registry_api.models import BaseTable

class SchemaEntities(BaseTable, table=True):
    __tablename__ = "schema_entities"
    name: str = Field(max_length=50, unique=True)


class Schemas(BaseTable, table=True):
    __tablename__ = "schemas"
    __table_args__ = (
        UniqueConstraint("name", "version", name="unique_schema_name_version"),
    )
    name: str = Field(max_length=50)
    version: str = Field(max_length=50)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_entity_id: int | None = Field(
        default=None, foreign_key="schema_entities.id"
    )

class DataAssets(BaseTable, table=True):
    __tablename__ = "data_assets"
    __table_args__ = (
        UniqueConstraint("name", "space_id", name="unique_data_asset_name_space_id"),
    )
    name: str | None = Field(default=None, max_length=254)
    location: str | None = Field(default=None, max_length=254, index=True)
    external_links: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    collections: List["Collections"] = Relationship(
        back_populates="data_assets",
        link_model=CollectionDataAssets,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )
    process_inputs: List["Processes"] = Relationship(
        back_populates="data_asset_inputs",
        link_model=ProcessInputs,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )

class Subjects(BaseTable, table=True):
    __tablename__ = "subjects"
    __table_args__ = (
        UniqueConstraint("name", "space_id", name="unique_subject_name_space_id"),
    )
    name: str = Field(max_length=254)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    acquisitions: List["Acquisitions"] = Relationship(
        back_populates="subjects",
        link_model=AcquisitionSubjects,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )

class Specimens(BaseTable, table=True):
    __tablename__ = "specimens"
    name: str = Field(max_length=254)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    subject_id: int | None = Field(
        default=None, foreign_key="subjects.id", index=True
    )
    acquisitions: List["Acquisitions"] = Relationship(
        back_populates="specimens",
        link_model=AcquisitionSpecimens,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )
    subject_procedures: List["SubjectProcedures"] = Relationship(
        back_populates="specimens",
        link_model=SubjectProcedureOutputs,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )
    specimen_procedures_inputs: List["SpecimenProcedures"] = Relationship(
        back_populates="specimen_inputs",
        link_model=SpecimenProcedureInputs,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )
    specimen_procedures_outputs: List["SpecimenProcedures"] = Relationship(
        back_populates="specimen_outputs",
        link_model=SpecimenProcedureOutputs,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )

class SpecimenProcedures(BaseTable, table=True):
    __tablename__ = "specimen_procedures"
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    specimen_inputs: List["Specimens"] = Relationship(
        back_populates="specimen_procedures_inputs",
        link_model=SpecimenProcedureInputs,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )
    specimen_outputs: List["Specimens"] = Relationship(
        back_populates="specimen_procedures_outputs",
        link_model=SpecimenProcedureOutputs,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )

class SubjectProcedures(BaseTable, table=True):
    __tablename__ = "subject_procedures"
    data: List[Dict[str, Any]] = Field(
        default_factory=list,
        sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    subject_id: int | None = Field(
        default=None, foreign_key="subjects.id", index=True
    )
    specimens: List["Specimens"] = Relationship(
        back_populates="subject_procedures",
        link_model=SubjectProcedureOutputs,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )

class Instruments(BaseTable, table=True):
    __tablename__ = "instruments"
    __table_args__ = (
        UniqueConstraint("name", "space_id", name="unique_instrument_name_space_id"),
    )
    name: str = Field(max_length=254)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )

class Acquisitions(BaseTable, table=True):
    __tablename__ = "acquisitions"
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    data_asset_id: int | None = Field(
        default=None, foreign_key="data_assets.id", index=True
    )
    instrument_id: int | None = Field(
        default=None, foreign_key="instruments.id", index=True
    )
    subjects: List["Subjects"] = Relationship(
        back_populates="acquisitions",
        link_model=AcquisitionSubjects,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )
    specimens: List["Specimens"] = Relationship(
        back_populates="acquisitions",
        link_model=AcquisitionSpecimens,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )

class QualityControls(BaseTable, table=True):
    __tablename__ = "quality_controls"
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    data_asset_id: int | None = Field(
        default=None, foreign_key="data_assets.id", index=True
    )

class Processes(BaseTable, table=True):
    __tablename__ = "processes"
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    output_data_asset_id: int | None = Field(
        default=None, foreign_key="data_assets.id", index=True
    )
    data_asset_inputs: List["DataAssets"] = Relationship(
        back_populates="process_inputs",
        link_model=ProcessInputs,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )
