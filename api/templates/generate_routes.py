import inspect
from biodata_registry_api.models import link_tables, admin, core
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from sqlalchemy import inspect as  sql_inspect

def to_snake_case(text):
    return ''.join(['_' + char.lower() if char.isupper() else char for char in text]).lstrip('_')

admin_classes = [
    name for name, obj in inspect.getmembers(admin, inspect.isclass)
    if obj.__module__ == admin.__name__
]

core_classes = [
    name for name, obj in inspect.getmembers(core, inspect.isclass)
    if obj.__module__ == core.__name__
]

link_table_classes = [
    (name, obj) for name, obj in inspect.getmembers(link_tables, inspect.isclass)
    if obj.__module__ == link_tables.__name__
]

base_admin_class_names = [
    c.replace("Create", "") for c in admin_classes if c.endswith("Create")
]

route_manifests = []
for c in base_admin_class_names:
    route_name = to_snake_case(c)
    if c.endswith("ty"):
        class_name = c.replace("ty", "ties")
    elif c.endswith("s"):
        class_name = f"{c}es"
    else:
        class_name = f"{c}s"
    plural_route_name = to_snake_case(class_name)
    class_create_name = f"{c}Create"
    class_update_name = f"{c}Update"
    route_manifests.append(
        {
            "module_name": "admin",
            "api_name": "admin",
            "route_name": route_name,
            "plural_route_name": plural_route_name,
            "class_name": class_name,
            "class_create_name": class_create_name,
            "class_update_name": class_update_name
        }
    )

base_core_class_names = [
    c.replace("Create", "") for c in core_classes if c.endswith("Create")
]

for c in base_core_class_names:
    route_name = to_snake_case(c)
    if c.endswith("ty"):
        class_name = c.replace("ty", "ties")
    elif c.endswith("s"):
        class_name = f"{c}es"
    else:
        class_name = f"{c}s"
    plural_route_name = to_snake_case(class_name)
    class_create_name = f"{c}Create"
    class_update_name = f"{c}Update"
    route_manifests.append(
        {
            "module_name": "core",
            "api_name": "core",
            "route_name": route_name,
            "plural_route_name": plural_route_name,
            "class_name": class_name,
            "class_create_name": class_create_name,
            "class_update_name": class_update_name
        }
    )

env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template('crud_template.py.j2')

for route_manifest in route_manifests:
    file_name = route_manifest["plural_route_name"]
    path_name = (
            Path("src") / "biodata_registry_api" / "routes" / f'{file_name}.py'
    )
    with open(path_name, 'w') as f:
        f.write(template.render(route_manifest))


#     if data_asset.collection_ids:
#         statement = select(Collections).where(
#             Collections.id.in_(data_asset.collection_ids)
#         )
#         results = await session.exec(statement)
#         collections = results.all()
#         row.collections = list(collections)
