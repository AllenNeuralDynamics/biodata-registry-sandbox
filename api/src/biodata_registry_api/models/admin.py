from biodata_registry_api.models. link_tables import CollectionDataAssets
from sqlmodel import Field, Relationship
from typing import List
from biodata_registry_api.models import BaseTable

class Users(BaseTable, table=True):
    __tablename__ = "users"
    name: str = Field(max_length=254)
    contact: str = Field(max_length=254, unique=True)

class Organizations(BaseTable, table=True):
    __tablename__ = "organizations"
    name: str = Field(max_length=254, unique=True)

class Spaces(BaseTable, table=True):
    __tablename__ = "spaces"
    name: str = Field(max_length=254)
    organization_id: int | None = Field(
        default=None, foreign_key="organizations.id"
    )

class SpaceAdmins(BaseTable, table=True):
    __tablename__ = "space_admins"
    user_id: int | None = Field(default=None, foreign_key="users.id")
    space_id: int | None = Field(default=None, foreign_key="spaces.id")

class OrganizationAdmins(BaseTable, table=True):
    __tablename__ = "organization_admins"
    user_id: int | None = Field(default=None, foreign_key="users.id")
    organization_id: int | None = Field(
        default=None, foreign_key="organizations.id"
    )

class Collections(BaseTable, table=True):
    __tablename__ = "collections"
    name: str = Field(max_length=254)
    description: str = Field(max_length=254)
    owner_id: int | None = Field(default=None, foreign_key="users.id")
    data_assets: List["DataAssets"] = Relationship(
        back_populates="collections",
        link_model=CollectionDataAssets,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )
