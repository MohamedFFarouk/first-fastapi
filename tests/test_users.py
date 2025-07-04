import email
from app.config import settings
from app import schemas
import pytest
from jose import jwt


def test_create_user(client):
    response = client.post(
        "/users/", json={"email": "testuser@example.com", "password": "testpassword"}
    )
    new_user = schemas.UserResponse(**response.json())
    assert new_user.email == "testuser@example.com"
    assert response.json().get("email") == "testuser@example.com"
    assert response.status_code == 201


def test_login_user(client, test_user):
    response = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    login_res = schemas.Token(**response.json())
    payload = jwt.decode(
        login_res.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    user_id = payload.get("user_id")
    assert user_id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert response.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrongemail@gmail.com", "password123", 403),
        ("sanjeev@gmail.com", "wrongpassword", 403),
        ("wrongemail@gmail.com", "wrongpassword", 403),
        (None, "password123", 403),
        ("sanjeev@gmail.com", None, 403),
    ],
)
def test_incorrect_login(client, test_user, email, password, status_code):
    response = client.post(
        "/login",
        data={"username": email, "password": password},
    )
    assert response.status_code == status_code
    assert response.json().get("detail") == "Invalid credentials"
