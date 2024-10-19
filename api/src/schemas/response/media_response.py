from pydantic import BaseModel, ConfigDict
from src.enums.media_name import MediaName


class MediaResponse(BaseModel):
    id: int
    name: MediaName
    description: str

    model_config = ConfigDict(from_attributes=True)
