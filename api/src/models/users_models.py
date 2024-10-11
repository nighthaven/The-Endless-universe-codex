import enum
import typing
import uuid
from datetime import datetime

from sqlalchemy import ARRAY, TIMESTAMP, Column, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from src.models import Base


class UserRole(enum.Enum):
    SUPERADMIN = "superadmin"
    ADMIN = "admin"
    EDITOR = "editor"
    MEMBER = "member"


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    roles = Column(ARRAY(Enum(UserRole)), nullable=False, default=[UserRole.MEMBER])

    def __init__(self, roles=None, **kwargs: typing.Any) -> None:
        super().__init__(**kwargs)

        self.roles = roles or [UserRole.MEMBER]
        if UserRole.SUPERADMIN in self.roles:
            self.roles.append(UserRole.ADMIN)
        if UserRole.ADMIN in self.roles:
            self.roles.append(UserRole.EDITOR)
