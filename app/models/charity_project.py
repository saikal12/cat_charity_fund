from sqlalchemy import Column, String, Text

from ..core.db import Base
from .base import BaseModel


class CharityProject(Base, BaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)