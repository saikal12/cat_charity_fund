from sqlalchemy import Date, TIMESTAMP, extract

from app.crud.base import CRUDBase
from app.models import CharityProject
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectUpdate)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, between, func, or_, select


class CRUDCharityproject(
        CRUDBase[CharityProject, CharityProjectCreate, CharityProjectUpdate]):

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[dict[str, str]]:
        project = await session.execute(
            select(
                CharityProject.name,
                (func.extract('epoch', CharityProject.close_date) -
                func.extract('epoch', CharityProject.create_date)).label('time_diff'),
                CharityProject.description
            ).where(CharityProject.fully_invested == True).order_by('time_diff')
        )
        return project.all()

charity_project_crud = CRUDCharityproject(CharityProject)
