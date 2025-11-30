from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_keywords():
    res = client.post("/keywords", json={"text": "Python is great and Python is popular for AI."})
    assert res.status_code == 200
    assert "keywords" in res.json()
