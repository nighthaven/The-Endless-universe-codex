from src.schemas.base.user_base import UserBase


class UserCreationForm(UserBase):
    password: str
