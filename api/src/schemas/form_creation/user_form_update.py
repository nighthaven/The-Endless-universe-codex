from typing import List

from pydantic import BaseModel
from src.models.users_models import UserRole


class UserFormUpdate(BaseModel):
    roles: List[UserRole]
