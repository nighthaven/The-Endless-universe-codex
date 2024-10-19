from pydantic import ConfigDict
from src.schemas.base.user_base import UserBase


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
