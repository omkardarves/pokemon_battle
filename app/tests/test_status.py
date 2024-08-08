from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_status():
    battle_id = "some-battle-id"
    response = client.get(f"/status/{battle_id}")
    assert response.status_code == 200
    assert "status" in response.json()
