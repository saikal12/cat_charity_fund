# app/models/user.py
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from cat_charity_fund.app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    pass