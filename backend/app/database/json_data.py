import json
from pathlib import Path
from typing import Any, Dict, List, Optional


DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "seed"


def load_records(filename: str) -> List[Dict[str, Any]]:
    path = DATA_DIR / filename
    try:
        with path.open(encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"JSON data file not found: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {path}: {error}") from error

    if not isinstance(records, list):
        raise ValueError(f"Expected a JSON array in {path}")
    return records


def get_record_by_id(filename: str, record_id: str) -> Optional[Dict[str, Any]]:
    return next(
        (record for record in load_records(filename) if record.get("_id") == record_id),
        None,
    )


def filter_records(
    filename: str, field: str, value: Any
) -> List[Dict[str, Any]]:
    return [
        record for record in load_records(filename) if record.get(field) == value
    ]
