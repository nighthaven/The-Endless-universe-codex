from pydantic import BaseModel, ConfigDict
from src.models.media_models import MediaName


class MediaFormCreation(BaseModel):
    name: MediaName
    description: str


class MediaResponseModel(BaseModel):
    id: int
    name: MediaName
    description: str

    model_config = ConfigDict(from_attributes=True)
