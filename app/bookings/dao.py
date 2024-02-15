from app.dao.base import BaseDAO
from datetime import date

from sqlalchemy import and_, func, insert, or_, select
from app.database import engine, async_session_maker

from app.bookings.models import Bookings
from app.hotels.rooms.models import Rooms

# from app.logger import logger

# class BookingDAO:
#
#     @classmethod
#     async def find_all(cls):
#         async with async_session_maker() as session:
#             quere = select(Bookings.__table__.columns)
#             result = await session.execute(quere)
#             return result.mappings().all()

class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(
            cls,
            user_id: int,
            room_id: int,
            date_from: date,
            date_to: date
    ):
        """WITH booked_rooms AS (
        SELECT * from bookings
        WHERE room_id = 1 AND
        (date_from >= '2023-05-15' AND date_from <= '2023-06-20') or
        (date_from <= '2023-05-15' AND date_to > '2023-06-20')
    )

        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
        LEFT JOIN booked_rooms on booked_rooms.room_id = rooms.id
        WHERE rooms.id = 1
        GROUP BY rooms.quantity, booked_rooms.room_id"""
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == room_id,
                    or_(
                        and_(Bookings.date_from >= date_from,
                             Bookings.date_from <= date_to),
                        and_(Bookings.date_from <= date_from,
                             Bookings.date_from > date_to
                             ),
                    )
                )
            ).cte('booked_rooms')

            # '''            SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
            #             LEFT JOIN booked_rooms on booked_rooms.room_id = rooms.id
            #             WHERE rooms.id = 1
            #             GROUP BY rooms.quantity, booked_rooms.room_id'''

            rooms_left = select(
                (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('room_left')
            ).select_from(Rooms).join(
                booked_rooms, booked_rooms.c.room_id == Rooms.id
            ).where(Rooms.id == room_id).group_by(
                Rooms.quantity, booked_rooms.c.room_id
            )

            # print(rooms_left.compile(engine, compile_kwargs={'literal_binds': True}))
            rooms_left = await session.execute(rooms_left)
            rooms_left: int = rooms_left.scalar()
            print(rooms_left)

    # @classmethod
    # async def find_all_with_images(cls, user_id: int):
    #     async with async_session_maker() as session:
    #         query = (
    #             select(
    #                 # __table__.columns нужен для отсутствия вложенности в ответе Алхимии
    #                 Bookings.__table__.columns,
    #                 Rooms.__table__.columns,
    #             )
    #             .join(Rooms, Rooms.id == Bookings.room_id, isouter=True)
    #             .where(Bookings.user_id == user_id)
    #         )
    #         result = await session.execute(query)
    #         return result.mappings().all()
    #
    # @classmethod
    # async def add(
    #     cls,
    #     user_id: int,
    #     room_id: int,
    #     date_from: date,
    #     date_to: date,
    # ):
    #     """
    #     WITH booked_rooms AS (
    #         SELECT * FROM bookings
    #         WHERE room_id = 1 AND
    #             (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
    #             (date_from <= '2023-05-15' AND date_to > '2023-05-15')
    #     )
    #     SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
    #     LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
    #     WHERE rooms.id = 1
    #     GROUP BY rooms.quantity, booked_rooms.room_id
    #     """
    #     # try:
    #     async with async_session_maker() as session:
    #         booked_rooms = (
    #             select(Bookings)
    #             .where(
    #                 and_(
    #                     Bookings.room_id == room_id,
    #                     or_(
    #                         and_(
    #                             Bookings.date_from >= date_from,
    #                             Bookings.date_from <= date_to,
    #                         ),
    #                         and_(
    #                             Bookings.date_from <= date_from,
    #                             Bookings.date_to > date_from,
    #                         ),
    #                     ),
    #                 )
    #             )
    #             .cte("booked_rooms")
    #         )
    #
    #         # """
    #         # SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
    #         # LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
    #         # WHERE rooms.id = 1
    #         # GROUP BY rooms.quantity, booked_rooms.room_id
    #         # """
    #
    #         get_rooms_left = (
    #             select(
    #                 (Rooms.quantity - func.count(booked_rooms.c.room_id).filter(booked_rooms.c.room_id.is_not(None))).label(
    #                     "rooms_left"
    #                 )
    #             )
    #             .select_from(Rooms)
    #             .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
    #             .where(Rooms.id == room_id)
    #             .group_by(Rooms.quantity, booked_rooms.c.room_id)
    #         )
    #
    #         # Рекомендую выводить SQL запрос в консоль для сверки
    #         print(get_rooms_left.compile(engine, compile_kwargs={"literal_binds": True}))
    #
    #         rooms_left = await session.execute(get_rooms_left)
    #         rooms_left: int = rooms_left.scalar()
    #         print(rooms_left)
    #
    #     # except:
    #     #     print('error')