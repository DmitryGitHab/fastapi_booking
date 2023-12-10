from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    rooms: Mapped[list["Rooms"]] = relationship(back_populates="hotel")

    def __str__(self):
        return f"Отель {self.name} {self.location[:30]}"


    # id = Column(Integer, primary_key=True)
    # name = Column(String, nullable=False)
    # location = Column(String, nullable=False)
    # services = Column(JSON)
    # room_quantity = Column(Integer, nullable=False)
    # image_id = Column(Integer)