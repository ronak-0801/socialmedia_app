import pytest
import bcrypt


def hash_password(password: str) -> str:
    """
    Hashes the given password using bcrypt and returns the hashed password.
    """
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")


SHARED_SEED_DATA_USER_DATA= {
    "users": [
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
        }]
}