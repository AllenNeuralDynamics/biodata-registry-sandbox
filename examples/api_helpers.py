from typing import Any

import requests


BASE_URL = "http://localhost:5000"


def register(session: requests.Session, endpoint: str, **kwargs) -> Any:
    response = session.post(f"{BASE_URL}{endpoint}", **kwargs)
    print(response.status_code)
    response.raise_for_status()
    if not response.content:
        return None
    return response.json()


def get(session: requests.Session, endpoint: str, **kwargs) -> Any:
    response = session.get(f"{BASE_URL}{endpoint}", **kwargs)
    response.raise_for_status()
    return response.json()


def find_record(
    rows: list[dict[str, Any]],
    **match_fields: Any,
) -> dict[str, Any] | None:
    for row in rows:
        if all(row.get(field) == value for field, value in match_fields.items()):
            return row
    return None


def get_or_register_record(
    session: requests.Session,
    *,
    endpoint: str,
    lookup_params: dict[str, Any],
    match_fields: dict[str, Any],
    create_params: dict[str, Any],
    data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    existing_rows = get(session, endpoint, params=lookup_params)
    existing_row = find_record(existing_rows, **match_fields)
    if existing_row is not None:
        return existing_row

    created_rows = register(
        session,
        endpoint,
        params=create_params,
        **({"json": data} if data is not None else {}),
    )
    return created_rows[0]
