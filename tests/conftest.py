'''confest.py'''

from typing import Any, Generator
from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from database import Base
from database import get_db 
from .seeding import Users_factory
from .db import engine, TestingSessionLocal
from pytest_factoryboy import register
from sqlalchemy.orm import Session


register(Users_factory)

# Fixture for SQLAlchemy session with SQLite database
@pytest.fixture(scope="function")
def app(db_session: Session) -> Generator[FastAPI, Any, None]:
    from src.app import app
    def override_get_db():
        db = db_session()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield app


# Fixture for TestClient for testing endpoints
@pytest.fixture(scope="function")
def client(app: FastAPI) -> Generator[TestClient, Any, None]:
    Base.metadata.create_all(bind=engine)

    with TestClient(app) as c:
        yield c
        Base.metadata.drop_all(bind=engine)


# Fixture for a persistent SQLAlchemy session
@pytest.fixture(scope="function")
def persistent_db_session():
    session = TestingSessionLocal()  # Assuming get_db_session() provides the session
    try:
        yield session
    finally:
        session.close()


# Fixture for Seeding the data to database
def persist_object(db: Session, object):
    db.add(object)
    db.commit()
    return object


pytest.persist_object = persist_object

@pytest.fixture
def seed(request: pytest.FixtureRequest, persistent_db_session: Session):
    marker = request.node.get_closest_marker("seed_data")
    if not (marker and marker.args and isinstance(marker.args, tuple)):
        print("_______________________________________________________")
        print("    There is no seed data or not a valid seed data.    ")
        print("-------------------------------------------------------")
        assert False

    for dataset in marker.args:
        entity_name, overridden_attributes = dataset

        factory = request.getfixturevalue(entity_name + "_factory")
        if isinstance(overridden_attributes, dict):
            pytest.persist_object(
                persistent_db_session, factory(**overridden_attributes)
            )
        elif isinstance(overridden_attributes, list):
            for attribute_set in overridden_attributes:
                pytest.persist_object(persistent_db_session, factory(**attribute_set))


