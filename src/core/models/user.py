from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import relationship
from core.types.user_id import UserIdType
from .base import Base
from .mixins.int_id_pk import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):

    phone_number: Mapped[str] = mapped_column(String(15), nullable=False, unique=True,)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
