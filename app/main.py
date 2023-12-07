from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class SHotel(BaseModel):
    adress: str
    name: str
    star: int
    # has_spa: bool

# @app.get("/hotels/", response_model=list[SHotel])
@app.get("/hotels/")
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
) -> list[SHotel]:
    hotels = [
        {
            'adress': "street, mt 101, Tyumen",
            'name': "MyLome",
            'star': 5,
        }
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date



@app.post("/bookings")
def add_booking(booking: SBooking):
    pass



# import requests
#
# r = requests.get(
#     "http://127.0.0.1:8000/hotels/5",
#     params={'date_from':'today', 'date_to':'tomorrow'}
# )