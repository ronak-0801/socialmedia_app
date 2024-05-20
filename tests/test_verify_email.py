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
    ("otps", SHARED_SEED_DATA["otps"]),
)
def test_verify_email_endpoint(client, seed):
    email_verification_data = {
        "email": "user1@example.com",
        "otp": "123456"
    }

    response = client.post("/verify_email", json=email_verification_data)

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Email verified successfully"
    assert "access_token" in data
    assert "refresh_token" in data
