from fastapi.testclient import TestClient
import pytest
from app import models
from app.database import get_db, Base
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.oauth2 import creat_access_token
from app.routers import auth

SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:ASdfghjkl12@localhost:5432/fastapi_test"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user2(client):
    user_data = {"email": "mohamedffaroukg123@gmail.com", "password": "ASdfghjkl12"}
    response = client.post("/users/", json=user_data)

    assert response.status_code == 201
    new_user = response.json()
    new_user["password"] = user_data["password"]

    return new_user


@pytest.fixture
def test_user(client):
    user_data = {"email": "mohamedffaroukg@gmail.com", "password": "ASdfghjkl12"}
    response = client.post("/users/", json=user_data)

    assert response.status_code == 201
    new_user = response.json()
    new_user["password"] = user_data["password"]

    return new_user


@pytest.fixture
def token(test_user):
    return creat_access_token(
        {"user_id": test_user["id"]},
    )


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}",
    }
    return client


@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [
        {
            "title": "First Post",
            "content": "Content of the first post",
            "owner_id": test_user["id"],
        },
        {
            "title": "Second Post",
            "content": "Content of the second post",
            "owner_id": test_user["id"],
        },
        {
            "title": "Third Post",
            "content": "Content of the third post",
            "owner_id": test_user["id"],
        },
        {
            "title": "Fourth Post",
            "content": "Content of the fourth post",
            "owner_id": test_user["id"],
        },
        {
            "title": "Fifth Post",
            "content": "Content of the fifth post",
            "owner_id": test_user["id"],
        },
        {
            "title": "Fifth Post",
            "content": "Content of the fifth post",
            "owner_id": test_user["id"],
        },
        {
            "title": "Fifth Post",
            "content": "Content of the fifth post",
            "owner_id": test_user2["id"],
        },
    ]

    session.add_all(models.Post(**post) for post in posts_data)
    session.commit()
    return session.query(models.Post).all()
