from fastapi.testclient import TestClient
from maana.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'profile revenue', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["roles"][0] == "profiler"
    refused = client.post("/agent/run", json={"goal": 'drop the staging table'}).json()
    assert refused["refused"] is True
