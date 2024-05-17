import datetime
import pytest
import bcrypt


def hash_password(password: str) -> str:
    """
    Hashes the given password using bcrypt and returns the hashed password.
    """
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")


SHARED_SEED_DATA= {
    "users":[
        {
            "id": 1,
            "name": "user1",
            "email": "user1@example.com",
            "password": hash_password("abcd") },
        {
            "id": 2,
            "name": "user2",
            "email": "user2@example.com",
            "password":hash_password("abcd")
        },
        {
            "id": 3,
            "name": "user3",
            "email": "user3@example.com",
            "password":hash_password("abcd")
        }],
        "otps": [
        {
            "email": "user1@example.com",
            "otp": "123456",
            "expiration_time": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)  
        },
        {
            "email": "user2@example.com",
            "otp": "123456",
            "expiration_time": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)  
        }
    ]
}
