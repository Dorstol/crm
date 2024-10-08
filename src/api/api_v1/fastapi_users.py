from fastapi_users import FastAPIUsers

from core.models import User
from core.types.user_id import UserIdType
from api.dependencies.auth.backend import auth_backend
from api.dependencies.auth.user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True)
current_super_user = fastapi_users.current_user(active=True, superuser=True)
