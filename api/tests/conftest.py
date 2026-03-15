from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> Generator[TestClient, Any, None]:
    """Creating a client for testing purposes."""

    from aind_registry_service_api.main import app

    with TestClient(app) as c:
        yield c
