from app.database import async_session_maker
from sqlalchemy import select

class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            quere = select(cls.model.__table__.columns)
            result = await session.execute(quere)
            return result.mappings().all()