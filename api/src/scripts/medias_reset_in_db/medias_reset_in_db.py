import sys
from pathlib import Path
from sqlalchemy import text

sys.path.append(str(Path(__file__).resolve().parents[3]))
import json
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from src.models import SessionLocal, get_db
from src.models.media_models import Media
from src.models.anomalies_models import Anomaly
from src.models.wonders_models import Wonder
from src.enums.media_name import MediaName

json_file_path = Path(__file__).parents[0] / "media.json"


with open(json_file_path, "r") as file:
    medias_data = json.load(file)


def delete_all_medias(db: Session):
    seq_name = db.execute(text("SELECT pg_get_serial_sequence('media', 'id')")).scalar()
    db.query(Anomaly).delete()
    db.query(Wonder).delete()
    db.query(Media).delete()
    db.execute(text(f"ALTER SEQUENCE {seq_name} RESTART WITH 1"))
    db.commit()


def import_all_medias(db: Annotated[Session, Depends(get_db)]):

    medias_to_insert = []
    for media_data in medias_data:
        name_list = [enum for enum in MediaName if media_data["name"] == enum.value]
        if not name_list:
            continue
        name = name_list[0]
        medias_to_insert.append(
            Media(
                name=name,
                description=media_data["description"],
            ),
        )
    if medias_to_insert:
        db.bulk_save_objects(medias_to_insert)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        delete_all_medias(db)
        import_all_medias(db)
    finally:
        db.close()
