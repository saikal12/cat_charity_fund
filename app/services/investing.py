from datetime import datetime

from sqlalchemy import select
from app.models import CharityProject, Donation
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union

def close_invest(obj):
    obj.fully_invested = True
    obj.close_date = datetime.now()


async def donation_investing(
        obj_in: Union[Donation, CharityProject],
        session: AsyncSession):

    obj_db = CharityProject if isinstance(obj_in, Donation) else Donation
    # отсортировать от новых к старым
    early_obj = await session.execute(select(obj_db).where(
        obj_db.fully_invested == False
    ).order_by(obj_db.create_date.desc()
    ))

    early_obj = early_obj.scalars().all()
    while early_obj and obj_in.full_amount > obj_in.invested_amount:
        investing_obj = early_obj.pop()
        need_investing = investing_obj.full_amount - investing_obj.invested_amount
        if obj_in.full_amount > need_investing:
            obj_in.full_amount = obj_in.full_amount - need_investing
            obj_in.invested_amount = need_investing
            investing_obj.invested_amount += obj_in.invested_amount
        else:
            obj_in.invested_amount = obj_in.full_amount
            close_invest(obj_in)
            investing_obj.invested_amount += obj_in.invested_amount
        if investing_obj.invested_amount == investing_obj.full_amount:
            close_invest(investing_obj)
        session.add(investing_obj)

    session.add(obj_in)
    await session.commit()
    await session.refresh(obj_in)
    return obj_in



