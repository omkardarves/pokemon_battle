from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_battle():
    response = client.post("/battle/", json={"pokemon_a": "pikachu", "pokemon_b": "bulbasaur"})
    assert response.status_code == 200
    assert "battle_id" in response.json()
