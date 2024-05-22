import pytest
from src.app import app
from fastapi.testclient import TestClient
from tests.data import SHARED_SEED_DATA


client = TestClient(app)


'''
testing add post
'''
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


'''
testing user is deleted or not found
'''
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
    response = client.post('/addpost', headers=auth_headers, json=data)
    print(response.json())
    assert "Failed to add post" in response.json()['detail']



'''
testing show post of user 
'''
@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
    ("posts", SHARED_SEED_DATA["posts"]),
)
@pytest.mark.parametrize('auth_headers', [1], indirect=True)
def test_show_post(seed,auth_headers):
    response = client.get('allpost', headers=auth_headers)
    print(response.json())
    assert 'post' in response.json()[0]
    assert 'caption' in response.json()[0]
    assert 'total_like' in response.json()[0]

@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
    ("posts", SHARED_SEED_DATA["posts"]),
)
@pytest.mark.parametrize('auth_headers', [1000], indirect=True)
def test_show_post_exception(seed,auth_headers):
    response = client.get('allpost', headers=auth_headers)
    print(response.json())
    assert "Failed to show post" in response.json()['detail']