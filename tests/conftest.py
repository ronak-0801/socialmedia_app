import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from typing import Any, Generator
from database import Base, get_db
from .seeding import Users_factory
from .db import engine, TestingSessionLocal
from pytest_factoryboy import register
from src.app import app
from src.utils.utils import create_access_token

register(Users_factory)


@pytest.fixture(scope="function")
def persistent_db_session() -> Session:
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# Fixture for SQLAlchemy session with SQLite database
@pytest.fixture(scope="function")
def db_session(persistent_db_session: Session) -> Generator[Session, Any, None]:
    try:
        yield persistent_db_session
        persistent_db_session.commit()
    except Exception as e:
        persistent_db_session.rollback()
        raise
    finally:
        persistent_db_session.close()

# Fixture for FastAPI app
@pytest.fixture(scope="function")
def app_fixture(db_session: Session) -> Generator[FastAPI, Any, None]:
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield app

# # Fixture for TestClient
@pytest.fixture(scope="function", autouse=True)
def client(app_fixture: FastAPI):
    Base.metadata.create_all(bind=engine)
    with TestClient(app_fixture) as c:
        yield c
    Base.metadata.drop_all(bind=engine)

# Helper function for seeding data
def persist_object(db: Session, obj):
    db.add(obj)
    db.commit()
    return obj

pytest.persist_object = persist_object

# Fixture for seeding data
@pytest.fixture
def seed(request: pytest.FixtureRequest, persistent_db_session: Session):
    marker = request.node.get_closest_marker("seed_data")
    if not (marker and marker.args and isinstance(marker.args, tuple)):
        assert False

    for dataset in marker.args:
        entity_name, overridden_attributes = dataset

        factory = request.getfixturevalue(entity_name + "_factory")
        if isinstance(overridden_attributes, dict):
            pytest.persist_object(persistent_db_session, factory(**overridden_attributes))
        elif isinstance(overridden_attributes, list):
            for attribute_set in overridden_attributes:
                pytest.persist_object(persistent_db_session, factory(**attribute_set))



@pytest.fixture
def auth_headers():
    user_id = 1# The ID of the user you want to authenticate as
    token = create_access_token(user_id)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    return headers