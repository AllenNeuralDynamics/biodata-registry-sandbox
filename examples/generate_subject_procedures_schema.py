import json
from pathlib import Path

from pydantic import RootModel

from aind_data_schema.core.procedures import Procedures


SCHEMA_DIR = Path(__file__).resolve().parent / "schema_definitions"
OUTPUT_PATH = SCHEMA_DIR / "subject_procedures.json"


def main() -> None:
    procedures_schema = Procedures.model_json_schema()
    subject_procedures_property = procedures_schema["properties"]["subject_procedures"]
    field_type = Procedures.model_fields["subject_procedures"].annotation
    subject_procedures_schema_model = RootModel[field_type]
    standalone_schema = subject_procedures_schema_model.model_json_schema()

    standalone_schema["title"] = subject_procedures_property.get(
        "title",
        standalone_schema.get("title"),
    )
    standalone_schema["description"] = subject_procedures_property.get(
        "description"
    )
    standalone_schema["default"] = subject_procedures_property.get("default", [])

    OUTPUT_PATH.write_text(
        json.dumps(standalone_schema, indent=3) + "\n",
        encoding="utf-8",
    )
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
