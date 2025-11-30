from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize():
    res = client.post("/summarize", json={"text": "AI is transforming the world of software engineering."})
    assert res.status_code == 200
    assert "summary" in res.json()
