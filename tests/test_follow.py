from fastapi.testclient import TestClient
from src.app import app
from tests.data import SHARED_SEED_DATA
import pytest

client = TestClient(app)


'''
add follower testing
'''
@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]))
@pytest.mark.parametrize('auth_headers', [1],indirect=True)
def test_add_follower(seed, auth_headers):
    response = client.post('/follow/2', headers=auth_headers)
    print(response.json())


    assert response.status_code == 200
    assert "successfully followed user" == response.json()


'''
show follower of user testing
'''
@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
    ("followers", SHARED_SEED_DATA["followers"]),
    )
@pytest.mark.parametrize('auth_headers', [1],indirect=True)
def test_show_follower(seed, auth_headers):
    # breakpoint()
    response = client.get('/show_follower', headers=auth_headers)
    print(response.json())

    assert response.status_code == 200
    assert "number_of_followers" in response.json()



'''
show following of user testing
'''
@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
    ("followers", SHARED_SEED_DATA["followers"]),
    )
@pytest.mark.parametrize('auth_headers', [1],indirect=True)
def test_show_following(seed, auth_headers):
    response = client.get('/show_following', headers=auth_headers)
    print(response.json())

    assert response.status_code == 200
    assert "number_of_followings" in response.json()