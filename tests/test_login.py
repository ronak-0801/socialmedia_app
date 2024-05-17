# import pytest
# from fastapi.testclient import TestClient
# from src.app import app
# from .data import SHARED_SEED_DATA_USER_DATA

# client = TestClient(app) 

# @pytest.mark.seed_data(
#     (
#         "users",
#         SHARED_SEED_DATA_USER_DATA["users"],
#     ),
# )
# def test_login(seed):

#     login_data = {
#         "username": "user1",
#         "password": "abcd",
#     }
#     response = client.post("/login", json=login_data)
#     print(response.json())
#     assert response.status_code == 200
#     assert "access_token" in response.json()


