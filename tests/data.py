import datetime
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
            "password":hash_password("abcd"),
            "is_active":False
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
        ],
        "passwords": [
        {
            "email": "user1@example.com",
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTk3NjAyfQ.PdtUym5ojRHEzk5i-jfWvcecw4hUsC7gUMBl9YVQ6Ks",
        }],
        "posts": [
            {
                "id" : 1,
                "post":1,
                "caption" : "user 1",
                "total_like" : 0,
                "uid": 1,
            },
            {
                "id" : 2,
                "post":1,
                "caption" : "user 2",
                "total_like" : 1,
                "uid": 2,
            },
        ],
        "likes": [
            {
                "id":1,
                "post_user_id" : 2,
                "user_id":1
            },
            {
                "id":2,
                "post_user_id" : 1,
                "user_id":2
            }
        ],
        "followers":[
            {
                "id":1,
                "followed_to":2,
                "following_by":1
            },
            {
                "id":2,
                "followed_to":1,
                "following_by":2
            },
        ],
        "comment":[
            {
                "id":1,
                "comment":"zdfdfsdf",
                "post_id":2,
                "user_id":1
            },
            {
                "id":2,
                "comment":"abababab",
                "post_id":2,
                "user_id":2
            }
        ]
}
