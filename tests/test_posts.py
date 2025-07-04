import pytest
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    posts = [schemas.PostOut(**post) for post in res.json()]

    assert res.status_code == 200
    assert isinstance(res.json(), list)
    assert len(posts) == len(test_posts)


def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401


def test_unauthorized_user_get_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_get_one_post_not_found(authorized_client, test_posts):
    res = authorized_client.get("/posts/999999")
    assert res.status_code == 404


def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert res.status_code == 200
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title


@pytest.mark.parametrize(
    "title, content, published",
    [
        ("new title", "new content", True),
        ("another title", "another content", False),
        (
            "title with special chars !@#$%^&*()",
            "content with special chars !@#$%^&*()",
            True,
        ),
    ],
)
def test_create_post(
    authorized_client, test_user, test_posts, title, content, published
):
    res = authorized_client.post(
        "/posts/", json={"title": title, "content": content, "published": published}
    )
    created_post = schemas.PostResponse(**res.json())

    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user["id"]


def test_create_post_default_published(authorized_client, test_user, test_posts):
    res = authorized_client.post(
        "/posts/", json={"title": "default title", "content": "default content"}
    )
    created_post = schemas.PostResponse(**res.json())

    assert res.status_code == 201
    assert created_post.title == "default title"
    assert created_post.content == "default content"
    assert created_post.published is True
    assert created_post.owner_id == test_user["id"]


def test_unauthorized_user_create_post(client, test_posts, test_user):
    res = client.post(
        "/posts/", json={"title": "default title", "content": "default content"}
    )
    assert res.status_code == 401


def test_unauthorized_user_delete_post(client, test_user, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_delete_post(authorized_client, test_user, test_posts):
    post_id = test_posts[0].id
    res = authorized_client.delete(f"/posts/{post_id}")
    assert res.status_code == 204

    get_res = authorized_client.get(f"/posts/{post_id}")
    assert get_res.status_code == 404


def test_delete_non_existent_post(authorized_client, test_user):
    res = authorized_client.delete("/posts/999999")
    assert res.status_code == 404


def test_delete_other_users_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[-1].id}")
    assert res.status_code == 403
    assert res.json().get("detail") == "Not authorized to perform requested action"


def test_update_post(authorized_client, test_user, test_posts):
    post_id = test_posts[0].id
    updated_data = {
        "title": "updated title",
        "content": "updated content",
        "published": False,
    }

    res = authorized_client.put(f"/posts/{post_id}", json=updated_data)
    updated_post = schemas.PostResponse(**res.json())

    assert res.status_code == 200
    assert updated_post.id == post_id
    assert updated_post.title == updated_data["title"]
    assert updated_post.content == updated_data["content"]
    assert updated_post.published == updated_data["published"]
    assert updated_post.owner_id == test_user["id"]


def tesT_update_other_user_post(authorized_client, test_user, test_posts):
    post_id = test_posts[-1].id
    updated_data = {
        "title": "updated title",
        "content": "updated content",
        "published": False,
    }
    res = authorized_client.put(f"/posts/{post_id}", json=updated_data)
    assert res.status_code == 403


def test_unauthorized_user_update_post(client, test_user, test_posts):
    updated_data = {
        "title": "updated title",
        "content": "updated content",
        "published": False,
    }
    res = client.put(f"/posts/{test_posts[0].id}", json=updated_data)
    assert res.status_code == 401


def test_update_non_existent_post(authorized_client, test_user):
    updated_data = {
        "title": "updated title",
        "content": "updated content",
        "published": False,
    }

    res = authorized_client.put("/posts/999999", json=updated_data)
    assert res.status_code == 404
