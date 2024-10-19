from pydantic import BaseModel
from src.enums.media_name import MediaName


class MediaFormCreation(BaseModel):
    name: MediaName
    description: str
