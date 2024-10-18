from typing import Optional

from pydantic import BaseModel, ConfigDict
from src.models.media_models import MediaName


class AnomalyBase(BaseModel):
    name: str
    description: str
    image: str
    media_name: MediaName


class AnomalyResponseModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    image: Optional[str]
    media_name: Optional[MediaName]

    model_config = ConfigDict(from_attributes=True)
