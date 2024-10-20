import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))
import json
from typing import Annotated, List, Optional

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.models import SessionLocal, get_db
from src.models.anomalies_models import Anomaly
from src.models.media_models import Media
from src.services.link_service import LinkService

json_file_path = Path(__file__).parents[1] / "json" / "anomalies.json"

with open(json_file_path, "r") as file:
    anomalies_data = json.load(file)


def delete_all_anomalies(db: Session):
    # Supprime toutes les lignes de la table Anomaly
    db.query(Anomaly).delete()
    db.commit()  # Confirme les changements


def import_all_anomalies(db: Annotated[Session, Depends(get_db)]):
    media_dict = {
        media.name.value: media.id for media in db.query(Media).all()  # type: ignore[union-attr]
    }
    link_service = LinkService()

    anomalies_to_insert = []
    for anomaly_data in anomalies_data:
        media_name = anomaly_data["media_name"]
        media_id = media_dict.get(media_name)
        if media_id:
            anomalies_to_insert.append(
                Anomaly(
                    name=anomaly_data["name"],
                    description=anomaly_data["description"],
                    image=link_service.get_image_anomalies_link(
                        media_name, anomaly_data["image"]
                    ),
                    media_id=media_id,
                )
            )
    if anomalies_to_insert:
        db.bulk_save_objects(anomalies_to_insert)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()  # Utilise directement le sessionmaker
    try:
        delete_all_anomalies(db)
        import_all_anomalies(db)
    finally:
        db.close()
    delete_all_anomalies(db)
    import_all_anomalies(db)
