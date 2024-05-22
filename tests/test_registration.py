import pytest
from sqlite3 import IntegrityError
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from src.app import app
from src.functionality.authentication.authentication import send_verification_email
# from src.utils.utils import send_email


client = TestClient(app) 

def get_user_data():
    user_data = {
            "name":"deadpool",
            "email": "ronbariy525@gmail.com",
            "password": "1234",
            "dob": "2024-05-14",
    }
    return user_data

'''Checking the user registration'''
def test_register_user():
    response = client.post(
        "/register_user",
        json= get_user_data()
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "User registered. Verification email sent."




'''checking if the user already exist'''
def test_duplicate_email():

    client.post("/register_user", json=get_user_data())
    
    duplicate_user_data = {
        "name": "Another User",
        "email": "ronbariy525@gmail.com",
        "password": "password789",
        "dob": "2000-01-01"
    }
    response = client.post("/register_user", json=duplicate_user_data)
    print(response.json())
    assert response.status_code == 500
    assert "Failed to register user" in response.json()["detail"]


'''checking if the data entered while registration was missing any field'''
def test_invalid_data():
    invalid_user_data = {
        "name": "Invalid User",
        "password": "password123",
        "dob": "1999-01-01"
    }
    response = client.post("/register_user", json=invalid_user_data)
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]

