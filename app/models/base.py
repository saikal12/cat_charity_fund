from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer


class BaseModel:
    __table_args__ = (
        CheckConstraint('invested_amount >= 0', name='check_invested_amount_positive'),
        CheckConstraint('full_amount >= invested_amount', name='check_invested_gte_full_amount')
    )
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0, nullable=False)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    close_date = Column(DateTime)

    class Meta:
        abstract = True
