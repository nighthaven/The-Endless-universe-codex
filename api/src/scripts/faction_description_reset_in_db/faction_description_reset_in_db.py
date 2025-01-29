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
from src.models.media_models import Media
from src.services.link_service import LinkService

json_file_path = Path(__file__).parents[0] / "faction_description.json"


with open(json_file_path, "r") as file:
    faction_descriptions_data = json.load(file)


def delete_all_faction_descriptions(db: Session):
    seq_name = db.execute(
        text("SELECT pg_get_serial_sequence('factions_descriptions', 'id')")
    ).scalar()
    db.query(FactionDescription).delete()
    db.execute(text(f"ALTER SEQUENCE {seq_name} RESTART WITH 1"))
    db.commit()


def import_all_faction_descriptions(db: Annotated[Session, Depends(get_db)]):
    media_dict = {media.id: media.name for media in db.query(Media).all()}
    link_service = LinkService()

    faction_informations_to_insert = []
    for i, description in enumerate(faction_descriptions_data, start=1):
        media_id = description["media_id"]
        media_name = media_dict.get(media_id).name  # type: ignore[union-attr]
        if media_name == "ENDLESS_SPACE":
            image = "ES1"
        if media_name == "ENDLESS_LEGEND":
            image = "EL"
        if media_name == "ENDLESS_SPACE_2":
            image = "ES2"
        image_link = link_service.get_image_faction_description_link(
            media_name, image, description["faction_id"]
        )
        faction_informations_to_insert.append(
            FactionDescription(
                faction_id=description["faction_id"],
                media_id=description["media_id"],
                description=description["description"],
                image_url=image_link,
                government=description["government"],
                ideology=description["ideology"],
                home_planet_id=description["home_planet_id"],
                affinity=description["affinity"],
                populations=description["populations"],
                traits=description["traits"],
                starting_technology=description["starting_technology"],
                units=description["units"],
                heroes=description["heroes"],
                major=description["major"],
                url=f"{settings.env_base_link}/endless/faction-description/{i}",
            )
        )
    if faction_informations_to_insert:
        db.bulk_save_objects(faction_informations_to_insert)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        delete_all_faction_descriptions(db)
        import_all_faction_descriptions(db)
    finally:
        db.close()
