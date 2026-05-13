from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class Device(Base):

    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    room = Column(String)
    status = Column(Boolean, default=False)