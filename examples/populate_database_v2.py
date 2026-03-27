from biodata_registry_api_client import (
    Configuration,
    ApiClient,
    AdminApi,
    CollectionCreate,
    CoreApi,
    DataAssetCreate,
    OrganizationCreate,
    UserCreate,
    SpaceCreate,
    SchemaEntityCreate,
    CollectionUpdate,
    SpaceAdminCreate
)

configuration = Configuration(
    host = "http://localhost:5000"
)

api_client = ApiClient(configuration)
admin_api = AdminApi(api_client)
core_api = CoreApi(api_client)

admin_api.create_user(
    UserCreate(name="Joe Smith", contact="joe.smith@example.com")
)

admin_api.create_user(
    UserCreate(name="Anna Apple", contact="anna.apple@example.com")
)

admin_api.create_organization(OrganizationCreate(name="AIND"))
admin_api.create_organization(OrganizationCreate(name="AIBS"))

admin_api.create_space(
    SpaceCreate(name="Space1", organization_id=1)
)

admin_api.create_space_admin(
    SpaceAdminCreate(space_id=1, user_id=1)
)

admin_api.create_collection(
    CollectionCreate(
        name="My Collection",
        description="My Collection description",
        owner_id=1,
        data_assets = [12]
    )
)

for schema_entity_name in [
    "acquisition",
    "data_description",
    "instrument",
    "subject_procedures",
    "specimen_procedures",
    "processing",
    "quality_control",
    "subject"
]:
    core_api.create_schema_entity(
        SchemaEntityCreate(name=schema_entity_name)
    )
