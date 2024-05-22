import pytest
from src.app import app
from fastapi.testclient import TestClient
from tests.data import SHARED_SEED_DATA

client = TestClient(app)


'''
Add comment testing
'''
@pytest.mark.seed_data(
        ("users", SHARED_SEED_DATA["users"]),
        ("posts", SHARED_SEED_DATA["posts"]),
)
@pytest.mark.parametrize('auth_headers',[1],indirect=True)
def test_add_comment(seed, auth_headers):
        response = client.post('/add_comment/2', headers=auth_headers, json={"comment":"ababababa"})
        print(response.json())

        assert response.status_code == 200
        assert "Comments added successfully" == response.json()

@pytest.mark.seed_data(
        ("users", SHARED_SEED_DATA["users"]),
        ("posts", SHARED_SEED_DATA["posts"]),
)
@pytest.mark.parametrize('auth_headers',[4],indirect=True)
def test_add_comment_user_not_found(seed, auth_headers):
        response = client.post('/add_comment/4', headers=auth_headers, json={"comment":"ababababa"})
        print(response.json())

        assert response.status_code == 500
        assert "Failed to add comment" == response.json()['detail']



'''
delete comment by post user testing
'''
@pytest.mark.seed_data(
        ("users", SHARED_SEED_DATA["users"]),
        ("posts", SHARED_SEED_DATA["posts"]),
        ("comments",SHARED_SEED_DATA["comment"])
)
@pytest.mark.parametrize('auth_headers',[2],indirect=True)
def test_delete_comment_by_user(seed, auth_headers):
        response = client.delete('/delete_comment/1', headers=auth_headers)

        assert response.status_code == 200
        assert "Comment deleted by post user" == response.json()



'''
delete comment by comment user testing
'''
@pytest.mark.seed_data(
        ("users", SHARED_SEED_DATA["users"]),
        ("posts", SHARED_SEED_DATA["posts"]),
        ("comments",SHARED_SEED_DATA["comment"])
)

@pytest.mark.parametrize('auth_headers',[1],indirect=True)
def test_delete_comment_by_cm_user(seed, auth_headers):
        response = client.delete('/delete_comment/1', headers=auth_headers)

        assert response.status_code == 200
        assert "Comment deleted by comment user"  == response.json()


@pytest.mark.seed_data(
        ("users", SHARED_SEED_DATA["users"]),
        ("posts", SHARED_SEED_DATA["posts"]),
        ("comments",SHARED_SEED_DATA["comment"])
)

@pytest.mark.parametrize('auth_headers',[1000],indirect=True)
def test_delete_comment_user_not_found(seed, auth_headers):
        response = client.delete('/delete_comment/10', headers=auth_headers)
        print(response.json())
        assert response.status_code == 500
        assert "Failed to delete comment"  == response.json()['detail']



