import pytest
from src.app import app
from fastapi.testclient import TestClient
from tests.data import SHARED_SEED_DATA

client = TestClient(app)


'''
testing add like 
'''
@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
    ("posts", SHARED_SEED_DATA["posts"]),
)
@pytest.mark.parametrize('auth_headers', [1],indirect=True)
def test_add_like(seed, auth_headers):
    response = client.post('/addlike/1', headers=auth_headers)
    print(response.json())
    assert "post" in response.json()
    

'''
testing unlike 
'''
@pytest.mark.seed_data(
    ("users", SHARED_SEED_DATA["users"]),
    ("posts", SHARED_SEED_DATA["posts"]),
    ("likes", SHARED_SEED_DATA["likes"]),
)
@pytest.mark.parametrize('auth_headers', [2],indirect=True)
def test_remove_like(seed, auth_headers):
    response = client.post('/addlike/1', headers=auth_headers)
    print(response.json())
    assert "post" in response.json()