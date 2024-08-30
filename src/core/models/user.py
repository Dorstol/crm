from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import relationship
from core.types.user_id import UserIdType
from .base import Base
from .mixins.int_id_pk import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .client import Client


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    clients = relationship("Client", back_populates="user")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
