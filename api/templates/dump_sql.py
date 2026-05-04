from sqlmodel import SQLModel, create_mock_engine
from biodata_registry_api.models.link_tables import *
from biodata_registry_api.models.admin import *
from biodata_registry_api.models.core import *
from biodata_registry_api.models.views import *


def dump_sql(filename: str = "init.sql"):
    # Define a dump function to write to the file
    def dump(sql, *multiparams, **params):
        with open(filename, "a") as f2:
            f2.write(str(sql.compile(dialect=engine.dialect)) + ";\n")

    # Create a mock engine (e.g., for PostgreSQL or SQLite)
    engine = create_mock_engine("postgresql://", dump)

    # Clear file if exists
    with open(filename, "w") as f:
        f.write(
            "-- SQLModel Generated Schema\n\n\c registry;\n\n"
        )

    # Dump the metadata
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    dump_sql()
