import pytest
from fastapi.testclient import TestClient
from ..endpoints import router

client = TestClient(router)

@pytest.mark.parametrize(
    "data, expected_status_code",
    [
        ({"amount": 1000, "customer_id": "123"}, 200),
        ({"amount": 1500, "customer_id": "456"}, 200),
        ({"customer_id": "invalid_id"}, 400),
        ({}, 400),
    ],
)
def test_create(data, expected_status_code):
    response = client.post("/loans/Create", json=data)
    assert response.status_code == expected_status_code

def test_list():
    response = client.get("/loans/List")
    assert response.status_code == 200

@pytest.mark.parametrize(
    "data, expected_status_code",
    [
        ({"loan_id": 1}, 200),
        ({"amount": 1000}, 200),
        ({"customer_id": "123"}, 200),
        ({"loan_id": 100}, 404),
        ({"amount": 999}, 404),
        ({"customer_id": "nonexistent"}, 404),
        ({}, 400),
    ],
)
def test_retrieve(data, expected_status_code):
    response = client.get("/loans/Retrieve", json=data)
    assert response.status_code == expected_status_code

@pytest.mark.parametrize(
    "data, expected_status_code",
    [
        ({"loan_id": 1, "amount": 2000}, 200),
        ({"loan_id": 100, "amount": 2000}, 404),
        ({}, 400),
    ],
)
def test_update(data, expected_status_code):
    response = client.put("/loans/Update", json=data)
    assert response.status_code == expected_status_code

@pytest.mark.parametrize(
    "data, expected_status_code",
    [
        ({"loan_id": 1}, 200),
        ({"loan_id": 100}, 404),
        ({}, 400),
    ],
)
def test_delete(data, expected_status_code):
    response = client.delete("/loans/Delete", json=data)
    assert response.status_code == expected_status_code
