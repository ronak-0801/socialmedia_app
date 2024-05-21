import pytest
from fastapi.testclient import TestClient
from src.app import app
from tests.data import SHARED_SEED_DATA
from src.utils.utils import create_access_token

client = TestClient(app)

token = create_access_token(1)
'''
Verify email of user using otp testing
'''
@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"])
    # ("passwords", SHARED_SEED_DATA["passwords"]),
)
def test_password_reset(seed):
    data = {
        "email": "user1@example.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTk3NjAyfQ.PdtUym5ojRHEzk5i-jfWvcecw4hUsC7gUMBl9YVQ6Ks",
        "new_password": "qwerty"
    }
    breakpoint()
    response = client.post("/password_reset",json=data)

    print( response.json())
    assert response.status_code == 200

