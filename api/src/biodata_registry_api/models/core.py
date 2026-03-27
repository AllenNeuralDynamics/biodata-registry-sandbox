from biodata_registry_api.models.link_tables import (
    CollectionDataAssets,
    # ProcessInputs,
    # SubjectProcedureOutputs,
    # AcquisitionSpecimens
)
from sqlmodel import SQLModel, Field, Column, Relationship
from typing import Dict, Any, List
from sqlalchemy.dialects.postgresql import JSONB

class SchemaEntityCreate(SQLModel):
    name: str = Field(max_length=50)

class SchemaEntityUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=50)

class SchemaEntities(SQLModel, table=True):
    __tablename__ = "schema_entities"
    name: str = Field(max_length=50)
    id: int | None = Field(default=None, primary_key=True)

class SchemaCreate(SQLModel):
    name: str = Field(max_length=50)
    version: str = Field(max_length=50)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_entity_id: int | None = Field(default=None)

class SchemaUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=50)
    version: str | None = Field(default=None, max_length=50)
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_entity_id: int | None = Field(default=None)

class Schemas(SQLModel, table=True):
    __tablename__ = "schemas"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    version: str = Field(max_length=50)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_entity_id: int | None = Field(
        default=None, foreign_key="schema_entities.id"
    )

class DataAssetCreate(SQLModel):
    name: str = Field(max_length=254)
    location: str = Field(max_length=254)
    external_links: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    # collection_ids: List[int] = Field(default=[])

class DataAssetUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    location: str | None = Field(default=None, max_length=254)
    external_links: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    # collection_ids: List[int] | None = Field(default=None)

class DataAssets(SQLModel, table=True):
    __tablename__ = "data_assets"
    id: int | None = Field(default=None, primary_key=True)
    name: str | None = Field(default=None, max_length=254)
    location: str | None = Field(default=None, max_length=254)
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
    # processes: List["Processes"] = Relationship(
    #     back_populates="processes", link_model=ProcessInputs
    # )

class SubjectCreate(SQLModel):
    name: str = Field(max_length=254)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )

class SubjectUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )

class Subjects(SQLModel, table=True):
    __tablename__ = "subjects"
    id: int | None = Field(default=None, primary_key=True)
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

class SpecimenCreate(SQLModel):
    name: str = Field(max_length=254)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    subject_id: int | None = Field(
        default=None, # foreign_key="subjects.id"
    )

class SpecimenUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    subject_id: int | None = Field(
        default=None, # foreign_key="subjects.id"
    )

class Specimens(SQLModel, table=True):
    __tablename__ = "specimens"
    id: int | None = Field(default=None, primary_key=True)
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
        default=None, foreign_key="subjects.id"
    )
#     subject_procedures: List["SubjectProcedures"] = Relationship(
#         back_populates="subject_procedures", link_model=SubjectProcedureOutputs
#     )
#     acquisitions: List["Acquisitions"] = Relationship(
#         back_populates="acquisitions", link_model=AcquisitionSpecimens
#     )
#
class SpecimenProcedureCreate(SQLModel):
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )

class SpecimenProcedureUpdate(SQLModel):
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )

class SpecimenProcedures(SQLModel, table=True):
    __tablename__ = "specimen_procedures"
    id: int | None = Field(default=None, primary_key=True)
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

class SubjectProcedureCreate(SQLModel):
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    subject_id: int | None = Field(
        default=None, # foreign_key="subjects.id"
    )

class SubjectProcedureUpdate(SQLModel):
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    subject_id: int | None = Field(
        default=None, # foreign_key="subjects.id"
    )

class SubjectProcedures(SQLModel, table=True):
    __tablename__ = "subject_procedures"
    id: int | None = Field(default=None, primary_key=True)
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
        default=None, foreign_key="subjects.id"
    )
#     specimens: List["Specimens"] = Relationship(
#         back_populates="specimens", link_model=SubjectProcedureOutputs
#     )
#
class InstrumentCreate(SQLModel):
    name: str = Field(max_length=254)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )

class InstrumentUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )

class Instruments(SQLModel, table=True):
    __tablename__ = "instruments"
    id: int | None = Field(default=None, primary_key=True)
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

class AcquisitionCreate(SQLModel):
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    data_asset_id: int | None = Field(
        default=None, # foreign_key="data_assets.id"
    )
    instrument_id: int | None = Field(
        default=None, # foreign_key="instruments.id"
    )

class AcquisitionUpdate(SQLModel):
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    data_asset_id: int | None = Field(
        default=None, # foreign_key="data_assets.id"
    )
    instrument_id: int | None = Field(
        default=None, # foreign_key="instruments.id"
    )

class Acquisitions(SQLModel, table=True):
    __tablename__ = "acquisitions"
    id: int | None = Field(default=None, primary_key=True)
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
        default=None, foreign_key="data_assets.id"
    )
    instrument_id: int | None = Field(
        default=None, foreign_key="instruments.id"
    )
#     specimens: List["Specimens"] = Relationship(
#         back_populates="specimens", link_model=AcquisitionSpecimens
#     )
#
class QualityControlCreate(SQLModel):
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    data_asset_id: int | None = Field(
        default=None, # foreign_key="data_assets.id"
    )

class QualityControlUpdate(SQLModel):
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    data_asset_id: int | None = Field(
        default=None, # foreign_key="data_assets.id"
    )

class QualityControls(SQLModel, table=True):
    __tablename__ = "quality_controls"
    id: int | None = Field(default=None, primary_key=True)
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
        default=None, foreign_key="data_assets.id"
    )

class ProcessCreate(SQLModel):
    data: Dict[str, Any] = Field(
        default_factory=dict,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    output_data_asset_id: int | None = Field(
        default=None, # foreign_key="data_assets.id"
    )

class ProcessUpdate(SQLModel):
    data: Dict[str, Any] | None = Field(
        default=None,
        # sa_column=Column(JSONB)
    )
    schema_id: int | None = Field(
        default=None, # foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, # foreign_key="spaces.id"
    )
    output_data_asset_id: int | None = Field(
        default=None, # foreign_key="data_assets.id"
    )

class Processes(SQLModel, table=True):
    __tablename__ = "processes"
    id: int | None = Field(default=None, primary_key=True)
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
        default=None, foreign_key="data_assets.id"
    )
#     data_assets: List["DataAssets"] = Relationship(
#         back_populates="data_assets", link_model=ProcessInputs
#     )
