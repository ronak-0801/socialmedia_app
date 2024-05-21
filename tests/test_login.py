import pytest
from fastapi.testclient import TestClient
from src.app import app
from .data import SHARED_SEED_DATA

client = TestClient(app) 

@pytest.mark.seed_data(
    (
        "users",
        SHARED_SEED_DATA["users"],
    ),
)
def test_login(seed):

    login_data = {
        "username": "user1",
        "password": "abcd",
    }
    response = client.post("/login", json=login_data)
    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()



@pytest.mark.seed_data(
    (
        "users",
        SHARED_SEED_DATA["users"],
    ),
)

def test_login_userdeacticated(seed):

    login_data = {
        "username": "user3",
        "password": "abcd",
    }
    response = client.post("/login", json=login_data)
    print(response.json())
    assert "User account is deactivated" in response.json()['detail']


@pytest.mark.seed_data(
    (
        "users",
        SHARED_SEED_DATA["users"],
    ),
)

def test_login_incorrect_email_or_pasword(seed):

    login_data = {
        "username": "user1",
        "password": "abcdd",
    }
    response = client.post("/login", json=login_data)
    print(response.json())
    assert response.json()['status_code'] == 401


@pytest.mark.seed_data(
    (
        "users",
        SHARED_SEED_DATA["users"],
    ),
)

def test_login_exeption(seed):

    login_data = {
        "username": "user",
        "password": "abcd",
    }
    response = client.post("/login", json=login_data)
    print(response.json())
    assert response.json()['detail'] == "Failed to login user"


