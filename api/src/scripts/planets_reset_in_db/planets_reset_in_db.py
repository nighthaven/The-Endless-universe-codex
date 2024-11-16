import sys
from pathlib import Path

from sqlalchemy import text

sys.path.append(str(Path(__file__).resolve().parents[3]))
import json
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from src.models import SessionLocal, get_db
from src.models.planets_model import Planet

json_file_path = Path(__file__).parents[0] / "planets.json"


with open(json_file_path, "r") as file:
    planets_data = json.load(file)


def delete_planets(db: Session):
    seq_name = db.execute(
        text("SELECT pg_get_serial_sequence('planet', 'id')")
    ).scalar()
    db.query(Planet).delete()
    db.execute(text(f"ALTER SEQUENCE {seq_name} RESTART WITH 1"))
    db.commit()


def import_planets(db: Annotated[Session, Depends(get_db)]):
    planets_to_insert = []
    for planet_data in planets_data:
        planets_to_insert.append(
            Planet(
                name=planet_data["name"],
                type=planet_data["type"],
                description=planet_data["description"],
            )
        )
    if planets_to_insert:
        db.bulk_save_objects(planets_to_insert)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        delete_planets(db)
        import_planets(db)
    finally:
        db.close()
