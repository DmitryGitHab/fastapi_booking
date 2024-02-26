from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        # orm_mode поменял название во 2 версии Pydantic
        # from_attributes = True
        model_config = ConfigDict(from_attributes=True)

class SBookingInfo(SBooking):
    image_id: int
    name: str
    description: Optional[str]
    services: list[str]

    class Config:
        # orm_mode поменял название во 2 версии Pydantic
        # from_attributes = True
        model_config = ConfigDict(from_attributes=True)


class SNewBooking(BaseModel):
    # user_id: int
    room_id: int
    date_from: date
    date_to: date