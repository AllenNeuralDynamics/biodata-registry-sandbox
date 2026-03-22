from biodata_registry_api.models. link_tables import CollectionDataAssets
from sqlmodel import SQLModel, Field, Column, Relationship
from typing import Dict, Any, List
from sqlalchemy.dialects.postgresql import JSONB

class SchemaEntityCreate(SQLModel):
    name: str = Field(max_length=50)

class SchemaEntityUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=50)

class SchemaEntities(SchemaEntityCreate, table=True):
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

class Schemas(SchemaCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
    data: Dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB)
    )
    schema_entity_id: int | None = Field(
        default=None, foreign_key="schemaentities.id"
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
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    # collections: List["Collections"] = Field(default=[])

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
        default=None, foreign_key="schemas.id"
    )
    space_id: int | None = Field(
        default=None, foreign_key="spaces.id"
    )
    # collections: List["Collections"] | None = Field(default=None)

class DataAssets(DataAssetCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
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
        back_populates="data_assets", link_model=CollectionDataAssets
    )
