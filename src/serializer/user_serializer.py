from pydantic import BaseModel, ConfigDict
from pydantic.networks import EmailStr
from src.models.users_models import UserRole
from typing import List
from datetime import datetime


class UserResponseModel(BaseModel):
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserCreationForm(UserResponseModel):
    password: str


class UserResponseModelWithRole(UserResponseModel):
    roles: List[UserRole]

    model_config = ConfigDict(from_attributes=True)


