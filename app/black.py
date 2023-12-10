class SHotel(BaseModel):
    adress: str
    name: str
    star: int



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