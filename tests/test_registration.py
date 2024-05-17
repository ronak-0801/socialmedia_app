
# from fastapi.testclient import TestClient

# from src.app import app


# # from src.resource.authentication.model import User
# # from src.resource.authentication.schema import User_schema, UserLoginSchema, Email_schema, PasswordResetSchema, Passwordtokenschema


# client = TestClient(app) 

# def get_user_data():
#     user_data = {
#             "name":"deadpool",
#             "email": "deadpoo0l@example.com",
#             "password": "chimichangas4life",
#             "dob": "2024-05-14",
#     }
#     return user_data

# '''Checking the user registration'''
# def test_register_user():
#     response = client.post(
#         "/register_user",
#         json= get_user_data()
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["message"] == "User registered. Verification email sent."




# '''checking if the user already exist'''
# def test_duplicate_email():

#     client.post("/register_user", json=get_user_data())
    
#     duplicate_user_data = {
#         "name": "Another User",
#         "email": "deadpoo0l@example.com",
#         "password": "password789",
#         "dob": "2000-01-01"
#     }
#     response = client.post("/register_user", json=duplicate_user_data)
#     print(response.json())
#     assert response.status_code == 400
#     assert "Email address already registered" in response.json()["detail"]


# '''checking if the data entered while registration was missing any field'''
# def test_invalid_data():
#     invalid_user_data = {
#         "name": "Invalid User",
#         "password": "password123",
#         "dob": "1999-01-01"
#     }
#     response = client.post("/register_user", json=invalid_user_data)
#     assert response.status_code == 422
#     assert "Field required" in response.json()["detail"][0]["msg"]





