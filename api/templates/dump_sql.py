from sqlmodel import SQLModel, create_mock_engine
from biodata_registry_api.models.link_tables import *
from biodata_registry_api.models.admin import *
from biodata_registry_api.models.core import *
# from biodata_registry_api.models.views import data_asset_view_statement

add_auto_update_timestamps = """
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';

DO $$
DECLARE
    t text;
BEGIN
    FOR t IN
        SELECT table_name
        FROM information_schema.columns
        WHERE column_name = 'updated_at'
          AND table_schema = 'public'
    LOOP
        EXECUTE format('
            CREATE TRIGGER trg_update_updated_at
            BEFORE UPDATE ON %I
            FOR EACH ROW
            EXECUTE PROCEDURE update_updated_at_column()', t);
    END LOOP;
END;
$$ language 'plpgsql';
"""

def dump_sql(filename: str = "init.sql"):
    def dump(sql, *multiparams, **params):
        with open(filename, "a") as f2:
            f2.write(str(sql.compile(dialect=engine.dialect)) + ";\n")

    engine = create_mock_engine("postgresql://", dump)
    with open(filename, "w") as f:
        f.write(
            r"\c registry;"
        )
        f.write(
            "\n\n-- SQLModel Generated Schema\n\n"
        )

    SQLModel.metadata.create_all(engine)

    from biodata_registry_api.models.views import data_asset_view_statement
    with open(filename, "a") as f:
        f.write("\n\n-- Handle created_at and updated_at fields\n\n")
        f.write(add_auto_update_timestamps)
        f.write("\n\n-- Views\n\n")
        f.write(data_asset_view_statement)


if __name__ == "__main__":
    dump_sql()
