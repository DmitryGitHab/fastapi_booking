import uvicorn
from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


class HotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool] = None,
            stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

class SHotel(BaseModel):
    adress: str
    name: str
    star: int
    # has_spa: bool

# @app.get("/hotels/", response_model=list[SHotel])
@app.get("/hotels/")
def get_hotels(
        search_args: HotelsSearchArgs = Depends()) :
    hotels = [
        {
            'adress': "street, mt 101, Tyumen",
            'name': "MyLome",
            'star': 5,
        }
    ]
    return search_args


# import requests
#
# r = requests.get(
#     "http://127.0.0.1:8000/hotels/5",
#     params={'date_from':'today', 'date_to':'tomorrow'}
# )

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True)