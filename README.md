# API Tests

Automated tests for a REST API, written in Python with pytest and requests.

The tests run against [JSONPlaceholder](https://jsonplaceholder.typicode.com), a free fake API made for practising.

## What the tests check

| Test | Request | Checks |
|---|---|---|
| `test_get_one_post` | `GET /posts/1` | Status 200, and the post has the right `id`, `userId` and a title |
| `test_get_all_posts` | `GET /posts` | Status 200, and exactly 100 posts come back |
| `test_missing_post_returns_404` | `GET /posts/99999` | A post that doesn't exist returns 404 (negative test) |
| `test_create_post` | `POST /posts` | Status 201 Created, the title comes back unchanged, and the new post gets id 101 |

## Run the tests

```bash
pip install -r requirements.txt
python -m pytest
```

## Built with

Python · pytest · requests
