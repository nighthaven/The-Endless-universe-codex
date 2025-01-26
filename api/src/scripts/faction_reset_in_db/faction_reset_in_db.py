import sys
from pathlib import Path

from sqlalchemy import text

sys.path.append(str(Path(__file__).resolve().parents[3]))
import json
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from src.config import settings
from src.models import SessionLocal, get_db
from src.models.faction_description_model import FactionDescription
from src.models.factions_models import Faction
from src.models.media_models import Media

json_file_path = Path(__file__).parents[0] / "factions.json"


with open(json_file_path, "r") as file:
    factions_data = json.load(file)


def delete_factions(db: Session):
    seq_name = db.execute(
        text("SELECT pg_get_serial_sequence('factions', 'id')")
    ).scalar()
    existing_faction_description = db.query(
        db.query(FactionDescription).exists()
    ).scalar()
    if existing_faction_description:
        db.query(Media).delete()
        db.query(FactionDescription).delete()
    db.query(Faction).delete()
    db.execute(text(f"ALTER SEQUENCE {seq_name} RESTART WITH 1"))
    db.commit()


def import_factions(db: Annotated[Session, Depends(get_db)]):
    faction_to_insert = []
    for i, faction_data in enumerate(factions_data, start=1):
        faction_to_insert.append(
            Faction(
                name=faction_data["name"],
                url=f"{settings.env_base_link}/endless/factions/{i}",
            )
        )
    if faction_to_insert:
        db.bulk_save_objects(faction_to_insert)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        delete_factions(db)
        import_factions(db)
    finally:
        db.close()
