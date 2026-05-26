from sqlmodel import SQLModel, Field
from typing import Sequence
from biodata_registry_api.models.crud import Page, PageFilter
from biodata_registry_api.models.admin import Users, Organizations, Spaces, Collections, SpaceAdmins, OrganizationAdmins
from fastapi_filter.contrib.sqlalchemy import Filter

class UserCreate(SQLModel):
    name: str = Field(max_length=254)
    contact: str = Field(max_length=254)

class UserUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    contact: str | None = Field(default=None, max_length=254)

class UsersPage(Page):
    results: Sequence[Users]

class UsersFilter(PageFilter):
    name__ilike: str | None = Field(default=None, max_length=254)
    contact__ilike: str | None = Field(default=None, max_length=254)
    class Constants:
        model = Users

class OrganizationCreate(SQLModel):
    name: str = Field(max_length=254)

class OrganizationUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)

class OrganizationsPage(Page):
    results: Sequence[Organizations]

class OrganizationsFilter(PageFilter):
    name__ilike: str | None = None
    class Constants:
        model = Organizations

class SpaceCreate(SQLModel):
    name: str = Field(max_length=254)
    organization_id: int | None = Field(
        default=None
    )

class SpaceUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    organization_id: int | None = Field(default=None)

class SpacesPage(Page):
    results: Sequence[Spaces]

class SpacesFilter(PageFilter):
    name__ilike: str | None = None
    class Constants:
        model = Spaces

class SpaceAdminCreate(SQLModel):
    user_id: int | None = Field(default=None)
    space_id: int | None = Field(default=None)

class SpaceAdminUpdate(SQLModel):
    user_id: int | None = Field(default=None)
    space_id: int | None = Field(default=None)

class SpaceAdminsPage(Page):
    results: Sequence[SpaceAdmins]

class SpaceAdminsFilter(PageFilter):
    class Constants:
        model = SpaceAdmins

class OrganizationAdminCreate(SQLModel):
    user_id: int | None = Field(default=None)
    organization_id: int | None = Field(default=None)

class OrganizationAdminUpdate(SQLModel):
    user_id: int | None = Field(default=None)
    organization_id: int | None = Field(default=None)

class OrganizationAdminsPage(Page):
    results: Sequence[OrganizationAdmins]

class OrganizationAdminsFilter(PageFilter):
    class Constants:
        model = OrganizationAdmins

class CollectionCreate(SQLModel):
    name: str = Field(max_length=254)
    description: str = Field(max_length=254)
    owner_id: int | None = Field(default=None)

class CollectionUpdate(SQLModel):
    name: str | None = Field(default=None, max_length=254)
    description: str | None = Field(default=None, max_length=254)
    owner_id: int | None = Field(default=None)

class CollectionsPage(Page):
    results: Sequence[Collections]

class CollectionsFilter(PageFilter):
    name__ilike: str | None = None
    description__ilike: str | None = None
    class Constants:
        model = Collections
