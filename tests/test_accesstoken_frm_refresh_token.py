
from fastapi.testclient import TestClient
import pytest
from src.app import app
client = TestClient(app)

@pytest.mark.parametrize('auth_headers', [1], indirect=True)
def test_ac_from_rf(auth_headers):
    response = client.post('/refresh_token',headers=auth_headers)
    data = response.json()

    print(response.json())
    assert response.status_code == 200
    assert "new_access_token" in data

