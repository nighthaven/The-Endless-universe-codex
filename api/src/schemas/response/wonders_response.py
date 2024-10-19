from pydantic import ConfigDict
from src.schemas.base.wonder_base import WonderBase


class WonderResponseModel(WonderBase):
    model_config = ConfigDict(from_attributes=True)
