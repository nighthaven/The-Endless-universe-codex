from abc import ABC
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from src.models import get_db


class BaseRepository(ABC):
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def save(self, object):
        self.db.add(object)
        self.db.commit()
        self.db.refresh(object)
        return object
