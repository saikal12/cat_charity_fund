from sqlalchemy import Column, String, Text

from .base import BaseModel
from ..core.db import Base


class CharityProject(Base, BaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

