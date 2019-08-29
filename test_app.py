import falcon.testing
import pytest

import app

@pytest.fixture()
def client():
    return falcon.testing.TestClient(app.create_app())

def test_hello_world(client):
    resp = client.simulate_get('/hello')
    assert resp.status_code == 200
    assert resp.json == {'hello': 'world'}
