import json
from pathlib import Path
from typing import get_args

from pydantic import RootModel

from aind_data_schema.core.quality_control import QualityControl


SCHEMA_DIR = Path(__file__).resolve().parent / "schema_definitions"
OUTPUT_PATH = SCHEMA_DIR / "quality_control_metric_schema.json"


def main() -> None:
    quality_control_schema = QualityControl.model_json_schema()
    metrics_property = quality_control_schema["properties"]["metrics"]
    metrics_field_type = QualityControl.model_fields["metrics"].annotation
    metric_type = get_args(metrics_field_type)[0]
    quality_control_schema_model = RootModel[metric_type]
    standalone_schema = quality_control_schema_model.model_json_schema()

    standalone_schema["title"] = metrics_property.get(
        "title",
        standalone_schema.get("title"),
    )

    OUTPUT_PATH.write_text(
        json.dumps(standalone_schema, indent=3) + "\n",
        encoding="utf-8",
    )
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
