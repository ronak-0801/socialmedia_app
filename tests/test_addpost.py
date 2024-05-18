from fastapi.testclient import TestClient
import pytest
from src.app import app
from tests.data import SHARED_SEED_DATA
client = TestClient(app)

@pytest.mark.seed_data(
    (
        "users",
        SHARED_SEED_DATA["users"],
    ),
)
@pytest.mark.parametrize('auth_headers', [1], indirect=True)
def test_add_post(seed,auth_headers):
    data = {
        'post' :'post 1',
        'caption' : 'post 1 user 1',
        'total_like' : 0
    }
    responce = client.post('/addpost', headers=auth_headers, json=data)

    print(responce.json())

    assert "post" in responce.json()

@pytest.mark.seed_data(
    (
        "users",
        SHARED_SEED_DATA["users"],
    ),
)
@pytest.mark.parametrize('auth_headers', [100], indirect=True)
def test_add_post_user_not_found(seed,auth_headers):
    data = {
        'post' :'post 1',
        'caption' : 'post 1 user 1',
        'total_like' : 0
    }
    responce = client.post('/addpost', headers=auth_headers, json=data)
    
    print(responce.json())

    assert "User is deleted or not found" in responce.json()


# @pytest.mark.seed_data(('users_factory', {}), ('posts_factory', {}))
# def test_get_posts():
#     response = client.get("/allpost/")
#     assert response.status_code == 200
#     print(response.json())
#     assert len(response.json()) > 0