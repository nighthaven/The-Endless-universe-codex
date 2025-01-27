import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.models import SessionLocal
from src.scripts.anomalies_reset_in_db.anomalies_reset_in_db import (
    delete_all_anomalies,
    import_all_anomalies,
)
from src.scripts.faction_description_reset_in_db.faction_description_reset_in_db import (
    delete_all_faction_descriptions,
    import_all_faction_descriptions,
)
from src.scripts.faction_reset_in_db.faction_reset_in_db import (
    delete_factions,
    import_factions,
)
from src.scripts.medias_reset_in_db.medias_reset_in_db import (
    delete_all_medias,
    import_all_medias,
)
from src.scripts.wonders_reset_in_db.wonders_reset_in_db import (
    delete_all_wonders,
    import_all_wonders,
)


def delete_all(db):
    delete_all_faction_descriptions(db)
    delete_all_anomalies(db)
    delete_all_wonders(db)
    delete_all_medias(db)
    delete_factions(db)


def import_all(db):
    import_all_medias(db)
    import_factions(db)
    import_all_wonders(db)
    import_all_anomalies(db)
    import_all_faction_descriptions(db)


if __name__ == "__main__":
    db = SessionLocal()
    try:
        delete_all(db)  # type: ignore[no-untyped-call]
        import_all(db)  # type: ignore[no-untyped-call]
    finally:
        db.close()
