from pydantic import BaseModel
from src.enums.media_name import MediaName

class MediaResponse(BaseModel):
    name: str

class FactionResponse(BaseModel):
    name: str

class FactionDescriptionBase(BaseModel):
    id: int
    faction: FactionResponse
    media: MediaResponse
    image_url: str
    major: bool

