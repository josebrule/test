import pytest
from fastapi.testclient import TestClient
from ..endpoints import router

client = TestClient(router)

@pytest.mark.parametrize(
    "data, expected_status_code",
    [
        ({"full_name": "John Doe", "email": "john@example.com"}, 200),
        ({"full_name": "Jane Doe", "email": "jane@example.com"}, 200),
        ({"email": "invalid_email"}, 400),
        ({}, 400),
    ],
)
def test_create(data, expected_status_code):
    response = client.post("/customers/Create", json=data)
    assert response.status_code == expected_status_code

def test_list():
    response = client.get("/customers/List")
    assert response.status_code == 200

@pytest.mark.parametrize(
    "data, expected_status_code",
    [
        ({"id": 1}, 200),
        ({"full_name": "John Doe"}, 200),
        ({"email": "john@example.com"}, 200),
        ({"id": 100}, 404),
        ({"full_name": "Non-existent"}, 404),
        ({"email": "nonexistent@example.com"}, 404),
        ({}, 400),
    ],
)
def test_retrieve(data, expected_status_code):
    response = client.get("/customers/Retrieve", json=data)
    assert response.status_code == expected_status_code

@pytest.mark.parametrize(
    "data, expected_status_code",
    [
        ({"id": 1, "full_name": "Updated Name", "email": "updated@example.com"}, 200),
        ({"id": 100, "full_name": "Updated Name", "email": "updated@example.com"}, 404),
        ({}, 400),
    ],
)
def test_update(data, expected_status_code):
    response = client.put("/customers/Update", json=data)
    assert response.status_code == expected_status_code

@pytest.mark.parametrize(
    "data, expected_status_code",
    [
        ({"id": 1}, 200),
        ({"full_name": "John Doe"}, 200),
        ({"email": "john@example.com"}, 200),
        ({"id": 100}, 404),
        ({"full_name": "Non-existent"}, 404),
        ({"email": "nonexistent@example.com"}, 404),
        ({}, 400),
    ],
)
def test_delete(data, expected_status_code):
    response = client.delete("/customers/Delete", json=data)
    assert response.status_code == expected_status_code
