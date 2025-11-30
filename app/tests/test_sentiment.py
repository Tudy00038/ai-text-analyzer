from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sentiment():
    res = client.post("/sentiment", json={"text": "I love this product!"})
    assert res.status_code == 200
    assert "label" in res.json()
