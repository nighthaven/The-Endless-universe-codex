import sys
from pathlib import Path

from sqlalchemy import text

sys.path.append(str(Path(__file__).resolve().parents[3]))
import json
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from src.models import SessionLocal, get_db
from src.models.factions_models import Faction

json_file_path = Path(__file__).parents[0] / "factions.json"


with open(json_file_path, "r") as file:
    factions_data = json.load(file)


def delete_all_faction(db: Session):
    seq_name = db.execute(
        text("SELECT pg_get_serial_sequence('factions', 'id')")
    ).scalar()
    db.query(Faction).delete()
    db.execute(text(f"ALTER SEQUENCE {seq_name} RESTART WITH 1"))
    db.commit()


def import_all_factions(db: Annotated[Session, Depends(get_db)]):
    faction_to_insert = []
    for faction_data in factions_data:
        faction_to_insert.append(
            Faction(
                name=faction_data["name"],
            )
        )
    if faction_to_insert:
        db.bulk_save_objects(faction_to_insert)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        delete_all_faction(db)
        import_all_factions(db)
    finally:
        db.close()
