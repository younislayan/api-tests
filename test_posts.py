import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_one_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    post = response.json()

    assert post["id"] == 1
    assert post["userId"] == 1
    assert post["title"] != ""

def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    posts = response.json()

    assert len(posts) == 100

def test_missing_post_returns_404():
    response = requests.get(f"{BASE_URL}/posts/99999")

    assert response.status_code == 404

def test_create_post():
    new_post = {
        "title": "My first post",
        "body": "Testing the API",
        "userId": 1,
    }

    response = requests.post(f"{BASE_URL}/posts", json=new_post)

    assert response.status_code == 201

    created = response.json()

    assert created["title"] == "My first post"
    assert created["id"] == 101