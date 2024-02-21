from fastapi import APIRouter, Request, Depends
from sqlalchemy import select

from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.bookings.schemas import SBooking
from app.exception import RoomFullyBooked
from app.hotels.rooms.models import Rooms
from app.database import async_session_maker
from app.users.dependencies import get_current_user
from app.users.models import Users
from datetime import date

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    print(user, type(user), user.email)
    return await BookingDAO.find_all(user_id=user.id)
    # return await BookingDAO.find_all()

@router.post('')
async def add_bookings(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomFullyBooked


# @router.get('')
# async def get_bookings(request: Request): #-> list[SBooking]
#     print(request.cookies)
#     print(request.url)
#     print(request.client)
#     return dir(request)
#     # return await BookingDAO.find_all()

# @router.get('')
# async def get_bookings():
#     return await BookingDAO.find_by_id(3)

# @router.get('')
# async def get_bookings():
#     return await BookingDAO.find_one_or_none(price=24500)

# @router.get('/{user_id}')
# async def get_bookings_join(user_id:int):
#     print(user_id)
#     async with async_session_maker() as session:
#         quere = select(Bookings.__table__.columns, Rooms.__table__.columns,).join(Rooms, Rooms.id == Bookings.room_id, isouter=True).where(Bookings.user_id == user_id)
#         result = await session.execute(quere)
#         return result.mappings().all()
#         # return user_id
#
# @router.post('/{booking_id}')
# def get_bookings(booking_id:int):
#     return booking_id