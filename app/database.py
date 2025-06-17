import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings  # your existing Pydantic settings

# ────────────────────────────────────────────────────────────────────────────────
# Choose the DB engine based on whether we are running in CI (GitHub Actions)
# ────────────────────────────────────────────────────────────────────────────────
if os.getenv("CI") == "true":
    # Lightweight SQLite for CI
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
    # Needed so SQLite works smoothly with SQLAlchemy in a multi-threaded context
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    # Full PostgreSQL URL for local/dev/prod
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{settings.database_username}:{settings.database_password}"
        f"@{settings.database_hostname}:{settings.database_port}/"
        f"{settings.database_name}"
    )
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session and Base stay exactly the same
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """FastAPI dependency that yields a SQLAlchemy session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
