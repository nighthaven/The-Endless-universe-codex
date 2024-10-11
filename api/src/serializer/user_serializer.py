from typing import List

from pydantic import BaseModel, ConfigDict
from pydantic.networks import EmailStr
from src.models.users_models import UserRole


class UserResponseModel(BaseModel):
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserCreationForm(UserResponseModel):
    password: str


class UserResponseModelWithRole(UserResponseModel):
    roles: List[UserRole]


class UpdateUserRoleRequest(BaseModel):
    roles: List[UserRole]


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
