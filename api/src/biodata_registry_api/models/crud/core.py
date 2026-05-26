from sqlmodel import SQLModel, Field
from typing import Dict, Any, List, Sequence

from biodata_registry_api.models.core import (
    Subjects,
    SchemaEntities,
    Schemas,
    DataAssets,
    Specimens,
    SpecimenProcedures,
    SubjectProcedures,
    Instruments,
    Acquisitions,
    Processes,
    QualityControls
)
from biodata_registry_api.models.crud import Page, PageFilter

class SchemaEntityCreate(SQLModel):
    name: str = Field(max_length=50)

class SchemaEntityUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=50)

class SchemaEntitiesPage(Page):
    results: Sequence[SchemaEntities]

class SchemaEntitiesFilter(PageFilter):
    name__ilike: str | None = None
    class Constants:
        model = SchemaEntities

class SchemaCreate(SQLModel):
    name: str = Field(max_length=50)
    version: str = Field(max_length=50)
    data: Dict[str, Any] = Field(
        default_factory=dict,
    )
    schema_entity_id: int | None = Field(default=None)

class SchemaUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=50)
    version: str | None = Field(default=None, max_length=50)
    data: Dict[str, Any] | None = Field(
        default=None,
    )
    schema_entity_id: int | None = Field(default=None)

class SchemasPage(Page):
    results: Sequence[Schemas]

class SchemasFilter(PageFilter):
    name__ilike: str | None = None
    version: str | None = Field(default=None, max_length=50)
    class Constants:
        model = Schemas

class DataAssetCreate(SQLModel):
    name: str = Field(max_length=254)
    location: str = Field(max_length=254)
    external_links: Dict[str, Any] = Field(
        default_factory=dict,
    )
    data: Dict[str, Any] = Field(
        default_factory=dict,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )

class DataAssetUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    location: str | None = Field(default=None, max_length=254)
    external_links: Dict[str, Any] | None = Field(
        default=None,
    )
    data: Dict[str, Any] | None = Field(
        default=None,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )

class DataAssetsPage(Page):
    results: Sequence[DataAssets]

class DataAssetsFilter(PageFilter):
    name__ilike: str | None = None
    location__ilike: str | None = None
    class Constants:
        model = DataAssets

class SubjectCreate(SQLModel):
    name: str = Field(max_length=254)
    data: Dict[str, Any] = Field(
        default_factory=dict,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )

class SubjectUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    data: Dict[str, Any] | None = Field(
        default=None,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )

class SubjectsPage(Page):
    results: Sequence[Subjects]

class SubjectsFilter(PageFilter):
    name__ilike: str | None = None
    class Constants:
        model = Subjects

class SpecimenCreate(SQLModel):
    name: str = Field(max_length=254)
    data: Dict[str, Any] = Field(
        default_factory=dict,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    subject_id: int | None = Field(
        default=None,
    )

class SpecimenUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    data: Dict[str, Any] | None = Field(
        default=None,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    subject_id: int | None = Field(
        default=None,
    )

class SpecimensPage(Page):
    results: Sequence[Specimens]

class SpecimensFilter(PageFilter):
    name__ilike: str | None = None
    class Constants:
        model = Specimens

class SpecimenProcedureCreate(SQLModel):
    data: Dict[str, Any] = Field(
        default_factory=dict,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )

class SpecimenProcedureUpdate(SQLModel):
    data: Dict[str, Any] | None = Field(
        default=None,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )

class SpecimenProceduresPage(Page):
    results: Sequence[SpecimenProcedures]

class SpecimenProceduresFilter(PageFilter):
    class Constants:
        model = SpecimenProcedures

class SubjectProcedureCreate(SQLModel):
    data: List[Dict[str, Any]] = Field(
        default_factory=list,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    subject_id: int | None = Field(
        default=None,
    )

class SubjectProcedureUpdate(SQLModel):
    data: List[Dict[str, Any]] | None = Field(
        default=None,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    subject_id: int | None = Field(
        default=None,
    )

class SubjectProceduresPage(Page):
    results: Sequence[SubjectProcedures]

class SubjectProceduresFilter(PageFilter):
    class Constants:
        model = SubjectProcedures

class InstrumentCreate(SQLModel):
    name: str = Field(max_length=254)
    data: Dict[str, Any] = Field(
        default_factory=dict,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )

class InstrumentUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    data: Dict[str, Any] | None = Field(
        default=None,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )

class InstrumentsPage(Page):
    results: Sequence[Instruments]

class InstrumentsFilter(PageFilter):
    name__ilike: str | None = None
    class Constants:
        model = Instruments

class AcquisitionCreate(SQLModel):
    data: Dict[str, Any] = Field(
        default_factory=dict,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    data_asset_id: int | None = Field(
        default=None,
    )
    instrument_id: int | None = Field(
        default=None,
    )

class AcquisitionUpdate(SQLModel):
    data: Dict[str, Any] | None = Field(
        default=None,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    data_asset_id: int | None = Field(
        default=None,
    )
    instrument_id: int | None = Field(
        default=None,
    )

class AcquisitionsPage(Page):
    results: Sequence[Acquisitions]

class AcquisitionsFilter(PageFilter):
    class Constants:
        model = Acquisitions

class QualityControlCreate(SQLModel):
    data: Dict[str, Any] = Field(
        default_factory=dict,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    data_asset_id: int | None = Field(
        default=None,
    )

class QualityControlUpdate(SQLModel):
    data: Dict[str, Any] | None = Field(
        default=None,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    data_asset_id: int | None = Field(
        default=None,
    )

class QualityControlsPage(Page):
    results: Sequence[QualityControls]

class QualityControlsFilter(PageFilter):
    class Constants:
        model = QualityControls

class ProcessCreate(SQLModel):
    data: Dict[str, Any] = Field(
        default_factory=dict,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    output_data_asset_id: int | None = Field(
        default=None,
    )

class ProcessUpdate(SQLModel):
    data: Dict[str, Any] | None = Field(
        default=None,
    )
    schema_id: int | None = Field(
        default=None,
    )
    space_id: int | None = Field(
        default=None,
    )
    output_data_asset_id: int | None = Field(
        default=None,
    )

class ProcessesPage(Page):
    results: Sequence[Processes]

class ProcessesFilter(PageFilter):
    class Constants:
        model = Processes
