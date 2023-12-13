

from sqlalchemy import select
from app.database import async_session_maker
from app.bookings.models import Bookings

class BookingDAO:

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            quere = select(Bookings.__table__.columns)
            result = await session.execute(quere)
            return result.mappings().all()