import os

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.models import get_db
from src.utils.Oauth2 import create_access_token
from tests.fixtures.anomalies_factory import AnomalyFactory
from tests.fixtures.faction_description_factory import FactionDescriptionFactory
from tests.fixtures.factions_factory import FactionFactory
from tests.fixtures.media_factory import MediaFactory
from tests.fixtures.planet_factory import PlanetFactory
from tests.fixtures.users_factory import UserFactory
from tests.fixtures.wonder_factory import WonderFactory

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOSTNAME')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
metadata = MetaData()


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def add_factories(db_session):
    UserFactory._meta.sqlalchemy_session = db_session
    MediaFactory._meta.sqlalchemy_session = db_session
    AnomalyFactory._meta.sqlalchemy_session = db_session
    WonderFactory._meta.sqlalchemy_session = db_session
    FactionFactory._meta.sqlalchemy_session = db_session
    PlanetFactory._meta.sqlalchemy_session = db_session
    FactionDescriptionFactory._meta.sqlalchemy_session = db_session


@pytest.fixture
def db_session():
    """Fixture qui crée une session de base de données pour les tests."""
    session = TestingSessionLocal()
    yield session
    session.close()


@pytest.fixture
def client(db_session):
    metadata.reflect(bind=engine)  # lie toutes donnée a la bdd
    metadata.drop_all(bind=engine)  # supprime tout
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
    command.upgrade(alembic_cfg, "head")

    add_factories(db_session)

    yield TestClient(app)


@pytest.fixture
def authenticated_client(client):
    user = UserFactory()
    access_token = create_access_token(data={"user_id": str(user.id)})
    client.headers = {"Authorization": f"Bearer {access_token}"}

    return client
