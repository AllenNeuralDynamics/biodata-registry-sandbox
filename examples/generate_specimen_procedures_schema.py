import json
from pathlib import Path

from pydantic import RootModel

from aind_data_schema.core.procedures import Procedures


SCHEMA_DIR = Path(__file__).resolve().parent / "schema_definitions"
OUTPUT_PATH = SCHEMA_DIR / "specimen_procedures.json"


def main() -> None:
    procedures_schema = Procedures.model_json_schema()
    specimen_procedures_property = procedures_schema["properties"][
        "specimen_procedures"
    ]
    field_type = Procedures.model_fields["specimen_procedures"].annotation
    specimen_procedures_schema_model = RootModel[field_type]
    standalone_schema = specimen_procedures_schema_model.model_json_schema()

    standalone_schema["title"] = specimen_procedures_property.get(
        "title",
        standalone_schema.get("title"),
    )
    standalone_schema["description"] = specimen_procedures_property.get(
        "description"
    )
    standalone_schema["default"] = specimen_procedures_property.get("default", [])

    OUTPUT_PATH.write_text(
        json.dumps(standalone_schema, indent=3) + "\n",
        encoding="utf-8",
    )
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
