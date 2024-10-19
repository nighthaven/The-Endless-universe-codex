from pydantic import BaseModel
from src.enums.media_name import MediaName


class WonderBase(BaseModel):
    name: str
    description: str
    image: str
    media_name: MediaName
