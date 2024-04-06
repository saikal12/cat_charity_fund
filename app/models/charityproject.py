from cat_charity_fund.app.core.db import Base
from sqlalchemy import Column, String, Text

from .base import BaseModel


class CharityProject(BaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

