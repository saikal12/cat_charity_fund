from datetime import datetime

from app.core.db import Base
from sqlalchemy import Column,Integer, Boolean, DateTime


class BaseModel:

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    close_date = Column(DateTime)

    class Meta:
        abstract = True
