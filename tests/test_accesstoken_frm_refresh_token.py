
from fastapi.testclient import TestClient
import pytest
from src.resource.authentication.model import User,Otp

from src.app import app
from tests.data import SHARED_SEED_DATA

client = TestClient(app)

# @pytest.mark.parametrize('auth_headers', [1], indirect=True)
# def test_ac_from_rf(auth_headers):
#     response = client.post('/refresh_token',headers=auth_headers)
#     data = response.json()

#     print(response.json())
#     # assert response.status_code == 200
#     assert "new_access_token" in data



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

    # assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Email verified successfully"
    assert "access_token" in data
    assert "refresh_token" in data

    # # Verify the user in the database is now marked as verified and active
    # db_session = next(get_db())
    # updated_user = db_session.query(User).filter_by(email=email_verification_data["email"]).first()
    # assert updated_user.is_email_verified
    # assert updated_user.is_active