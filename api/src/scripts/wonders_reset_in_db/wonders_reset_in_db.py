import sys
from pathlib import Path

from sqlalchemy import text

sys.path.append(str(Path(__file__).resolve().parents[3]))
import json
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from src.enums.media_name import MediaName
from src.models import SessionLocal, get_db
from src.models.media_models import Media
from src.models.wonders_models import Wonder
from src.services.link_service import LinkService
from src.utils.enum_utils import get_enum_key_by_value

json_file_path = Path(__file__).parents[0] / "wonders.json"


with open(json_file_path, "r") as file:
    wonders_data = json.load(file)


def delete_all_wonders(db: Session):
    seq_name = db.execute(
        text("SELECT pg_get_serial_sequence('wonder', 'id')")
    ).scalar()
    db.query(Wonder).delete()
    db.execute(text(f"ALTER SEQUENCE {seq_name} RESTART WITH 1"))
    db.commit()


def import_all_wonders(db: Annotated[Session, Depends(get_db)]):
    media_dict = {
        media.name.value: media.id for media in db.query(Media).all()  # type: ignore[union-attr]
    }
    link_service = LinkService()

    wonders_to_insert = []
    for wonder_data in wonders_data:
        media_name = wonder_data["media_name"]
        media_name_object = get_enum_key_by_value(MediaName, media_name)  # type: ignore[no-untyped-call]
        media_id = media_dict.get(media_name)
        if media_id:
            wonders_to_insert.append(
                Wonder(
                    name=wonder_data["name"],
                    description=wonder_data["description"],
                    image=link_service.get_image_wonders_link(
                        media_name_object, wonder_data["image"]
                    ),
                    media_id=media_id,
                )
            )
    if wonders_to_insert:
        db.bulk_save_objects(wonders_to_insert)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        delete_all_wonders(db)
        import_all_wonders(db)
    finally:
        db.close()
