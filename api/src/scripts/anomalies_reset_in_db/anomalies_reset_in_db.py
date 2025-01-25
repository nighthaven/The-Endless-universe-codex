import os
import sys
from pathlib import Path

from sqlalchemy import text

sys.path.append(str(Path(__file__).resolve().parents[3]))
import json
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from src.config import settings
from src.enums.media_name import MediaName
from src.models import SessionLocal, get_db
from src.models.anomalies_models import Anomaly
from src.models.media_models import Media
from src.services.link_service import LinkService
from src.utils.enum_utils import get_enum_key_by_value

json_file_path = Path(__file__).parents[0] / "anomalies.json"


with open(json_file_path, "r") as file:
    anomalies_data = json.load(file)


def delete_all_anomalies(db: Session):
    seq_name = db.execute(
        text("SELECT pg_get_serial_sequence('anomaly', 'id')")
    ).scalar()
    db.query(Anomaly).delete()
    db.execute(text(f"ALTER SEQUENCE {seq_name} RESTART WITH 1"))
    db.commit()


def import_all_anomalies(db: Annotated[Session, Depends(get_db)]):
    media_dict = {
        media.name.value: media.id for media in db.query(Media).all()  # type: ignore[union-attr]
    }
    link_service = LinkService()

    anomalies_to_insert = []
    for i, anomaly_data in enumerate(anomalies_data, start=1):
        media_name = anomaly_data["media_name"]
        media_name_object = get_enum_key_by_value(MediaName, media_name)  # type: ignore[no-untyped-call]
        media_id = media_dict.get(media_name)
        if media_id:
            anomalies_to_insert.append(
                Anomaly(
                    name=anomaly_data["name"],
                    description=anomaly_data["description"],
                    image=link_service.get_image_anomalies_link(
                        media_name_object, anomaly_data["image"]
                    ),
                    media_id=media_id,
                    url=f"{settings.env_base_link}/endless/anomaly/{i}",
                )
            )
    if anomalies_to_insert:
        db.bulk_save_objects(anomalies_to_insert)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        delete_all_anomalies(db)
        import_all_anomalies(db)
    finally:
        db.close()
