from fastapi.testclient import TestClient
from backend.app.endpoints.endpoints import app

client = TestClient(app)

def test_calculate_empty_string_returns_zero():
    response = client.post("/api/calculate", json={"numbers":""})
    assert response.status_code == 200
    assert response.json() == {"result": 0}


def test_calculate_invalid_input():
    response = client.post("/api/calculate", json={"numbers": "1,\n"})
    assert response.status_code == 400
    assert "Invalid input" in response.json()["detail"]