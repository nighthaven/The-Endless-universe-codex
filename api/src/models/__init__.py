# src/models/__init__.py
# mypy: ignore-errors

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.config import settings


def install_models() -> None:
    from src.models import (
        anomalies_models,
        faction_description_model,
        factions_models,
        media_models,
        planets_model,
        users_models,
        wonders_models,
    )


SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
