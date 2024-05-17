
from fastapi.testclient import TestClient
import pytest

from src.app import app
from .data import SHARED_SEED_DATA_USER_DATA

client = TestClient(app)


@pytest.mark.seed_data(
    (
        "users",
        SHARED_SEED_DATA_USER_DATA["users"],
    ),
)
@pytest.mark.parametrize('auth_headers', [1], indirect=True)

def test_delete_user(seed, auth_headers):
    response = client.delete('/delete_user',headers=auth_headers)
    data = response.json()

    print(response.json())
    assert response.status_code == 200

    assert "User deleted successfully" == data["message"]


@pytest.mark.seed_data(
    (
        "users",
        SHARED_SEED_DATA_USER_DATA["users"],
    ),
)
@pytest.mark.parametrize('auth_headers', [2000], indirect=True)
def test_delete_user_not_found(seed, auth_headers):
    response = client.delete('/delete_user', headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["detail"] == "User not found"
    assert response.json()["status_code"] == 404
