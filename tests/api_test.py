import pytest
from database import Base
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app import app
from database import get_db 
from sqlalchemy.pool import StaticPool

# from src.resource.authentication.model import User
# from src.resource.authentication.schema import User_schema, UserLoginSchema, Email_schema, PasswordResetSchema, Passwordtokenschema

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


client = TestClient(app)  
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield  # Run tests
    # Base.metadata.drop_all(bind=engine)


# def setup():
#     Base.metadata.create_all(bind=engine)

# def teardown():
#     Base.metadata.drop_all(bind=engine)

# '''Checking the user registration'''
# def test_register_user():
#     response = client.post(
#         "/register_user",
#         json={"name":"string","email": "deadpoo0l@exxample.com", "password": "chimichangas4life",  "dob": "2024-05-14"
# }
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["message"] == "User registered. Verification email sent."




# '''checking if the user already exist'''
# def test_duplicate_email():
#     existing_user_data = {
#         "name": "Jane Doe",
#         "email": "jane@example.com",
#         "password": "password456",
#         "dob": "1995-01-01"
#     }
#     client.post("/register_user", json=existing_user_data)
    
#     duplicate_user_data = {
#         "name": "Another User",
#         "email": "jane@example.com",
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
#         # Missing 'email' field
#         "password": "password123",
#         "dob": "1999-01-01"
#     }
#     response = client.post("/register_user", json=invalid_user_data)
#     assert response.status_code == 422
#     assert "Field required" in response.json()["detail"][0]["msg"]






'''Login'''
def test_login():
    # First, let's register a user
    register_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "securepassword",
        "dob": "1990-01-01",
        "is_active":True
    }
    client.post("/register_user", json=register_data)


    # Now, let's attempt to login with the registered user's credentials
    login_data = {
        "username": "John Doe",
        "password": "securepassword",
        # "is_active":True
    }
    response = client.post("/login", json=login_data)
    print(response.json())
    # Assert that the response is successful (status code 200) and contains a token
    assert response.status_code == 200
    assert "access_token" in response.json()


