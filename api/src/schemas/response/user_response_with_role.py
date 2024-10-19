from typing import List

from src.models.users_models import UserRole
from src.schemas.response.user_response import UserResponse


class UserResponseModelWithRole(UserResponse):
    roles: List[UserRole]
