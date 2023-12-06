from fastapi import FastAPI, Query
from typing import Optional
from datetime import date

app = FastAPI()

@app.get("/hotels/")
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
):
    return f"{location}, {date_from}, {date_to}, {has_spa}, {stars}"


# import requests
#
# r = requests.get(
#     "http://127.0.0.1:8000/hotels/5",
#     params={'date_from':'today', 'date_to':'tomorrow'}
# )