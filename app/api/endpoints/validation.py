from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    project = await session.execute(
        select(CharityProject.id).where(
            CharityProject.name == project_name
        )
    )
    existing_project = project.scalar()

    if existing_project is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )


async def check_project_exists(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    project = await charity_project_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return project


async def check_project_closed(
        fully_invested: bool
):
    if fully_invested is True:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )


async def check_full_amount(
        full_amount: int,
        project: CharityProject,
):
    if full_amount < project.invested_amount:
        raise HTTPException(
            status_code=400,
            detail='Нелья установить значение '
                   'full_amount меньше уже вложенной суммы.'
        )


async def check_before_delete(
        project: CharityProject
):
    if project.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, '
                   'не подлежит удалению!'
        )
    return project
