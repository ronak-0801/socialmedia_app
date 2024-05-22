import pytest
from fastapi.testclient import TestClient
from src.app import app
from tests.data import SHARED_SEED_DATA

client = TestClient(app)

'''
Verify email of user using otp testing
'''
@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
    ("passwords", SHARED_SEED_DATA["passwords"]),
)
def test_password_reset(seed):
    data = {
        "email": "user1@example.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTk3NjAyfQ.PdtUym5ojRHEzk5i-jfWvcecw4hUsC7gUMBl9YVQ6Ks",
        "new_password": "qwerty"
    }
    response = client.post("/password_reset",json=data)

    print( response.json())
    assert response.status_code == 200
    assert {"message": "Password reset successfully"} == response.json()


@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
    ("passwords", SHARED_SEED_DATA["passwords"]),
)
def test_password_reset_user_not_found():
    data = {
        "email": "user2@example.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTk3NjAyfQ.PdtUym5ojRHEzk5i-jfWvcecw4hUsC7gUMBl9YVQ6Ks",
        "new_password": "qwerty"
    }
    # breakpoint()
    response = client.post("/password_reset",json=data)

    print( response.json())
    assert response.status_code == 500
    assert "Failed to reset password" == response.json()['detail']


@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
)
def test_generate_password_reset_token(seed):
    data = {"email":"user2@example.com"}
    response = client.post("/password_reset_token",json=data)
    print(response.json())
    assert response.status_code == 200
    assert "Password reset email sent successfully" in response.json()['message']

@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
)
def test_generate_password_user_not_found(seed):
    data = {"email":"user@example.com"}
    response = client.post("/password_reset_token",json=data)
    print(response.json())
    assert response.status_code == 500
    assert "Failed to generate password reset token" in response.json()['detail']