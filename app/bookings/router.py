from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.models import Bookings
from app.database import async_session_maker

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)

@router.get('')
async def get_bookings():
    async with async_session_maker() as session:
        quere = select(Bookings.__table__.columns)
        result = await session.execute(quere)
        return result.mappings().all()


@router.post('/{booking_id}')
def get_bookings(booking_id):
    return booking_id