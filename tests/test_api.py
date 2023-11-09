from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_check() -> None:
    """
    Test the health check endpoint of the API.

    Sends a GET request to the '/health-check' endpoint and asserts that the response
    status code is 200 and that the response data contains a 'status' key with the value 'ok'.
    """
    response = client.get(
        "/health-check",
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["status"] == "ok"
