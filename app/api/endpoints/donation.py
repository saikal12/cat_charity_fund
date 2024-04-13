from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import (DonationCreate, DonationCreateResponse,
                                  DonationDB)
from app.services.investing import donation_investing

router = APIRouter()


@router.get('/', response_model=list[DonationDB],
            dependencies=[Depends(current_superuser)])
async def get_all_donations(session: AsyncSession = Depends(get_async_session)):
    """Только для суперюзеров."""
    donations = await donation_crud.get_multi(session)
    return donations


@router.get('/my', response_model=list[DonationCreateResponse])
async def get_user_donations(
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session)
):
    my_donations = await donation_crud.get_user_donation(user.id, session)
    return my_donations


@router.post('/', response_model=DonationCreateResponse)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    donation = await donation_crud.create(donation, session, user)
    return await donation_investing(donation, session)
