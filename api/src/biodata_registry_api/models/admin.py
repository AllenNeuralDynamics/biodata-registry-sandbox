from biodata_registry_api.models. link_tables import CollectionDataAssets
from sqlmodel import SQLModel, Field, Relationship
from typing import List

class UserCreate(SQLModel):
    name: str = Field(max_length=254)
    contact: str = Field(max_length=254)

class UserUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    contact: str | None = Field(default=None, max_length=254)

class Users(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=254)
    contact: str = Field(max_length=254)

class OrganizationCreate(SQLModel):
    name: str = Field(max_length=254)

class OrganizationUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)

class Organizations(SQLModel, table=True):
    __tablename__ = "organizations"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=254)

class SpaceCreate(SQLModel):
    name: str = Field(max_length=254)
    organization_id: int | None = Field(
        default=None
    )

class SpaceUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    organization_id: int | None = Field(default=None)

class Spaces(SQLModel, table=True):
    __tablename__ = "spaces"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=254)
    organization_id: int | None = Field(
        default=None, foreign_key="organizations.id"
    )

class SpaceAdminCreate(SQLModel):
    user_id: int | None = Field(default=None)
    space_id: int | None = Field(default=None)

class SpaceAdminUpdate(SQLModel):
    user_id: int | None = Field(default=None)
    space_id: int | None = Field(default=None)

class SpaceAdmins(SQLModel, table=True):
    __tablename__ = "space_admins"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id")
    space_id: int | None = Field(default=None, foreign_key="spaces.id")

class OrganizationAdminCreate(SQLModel):
    user_id: int | None = Field(default=None)
    organization_id: int | None = Field(default=None)

class OrganizationAdminUpdate(SQLModel):
    user_id: int | None = Field(default=None)
    organization_id: int | None = Field(default=None)

class OrganizationAdmins(SQLModel, table=True):
    __tablename__ = "organization_admins"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id")
    organization_id: int | None = Field(
        default=None, foreign_key="organizations.id"
    )

class CollectionCreate(SQLModel):
    name: str = Field(max_length=254)
    description: str = Field(max_length=254)
    owner_id: int | None = Field(default=None)
    # data_assets: List[int] = Field(default=[])

class CollectionUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    description: str | None = Field(default=None, max_length=254)
    owner_id: int | None = Field(default=None)
    # data_assets: List[int] | None = Field(default=None)

class Collections(SQLModel, table=True):
    __tablename__ = "collections"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=254)
    description: str = Field(max_length=254)
    owner_id: int | None = Field(default=None, foreign_key="users.id")
    data_assets: List["DataAssets"] = Relationship(
        back_populates="collections",
        link_model=CollectionDataAssets,
        sa_relationship_kwargs={'lazy': 'selectin'}
    )
