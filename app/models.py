from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    path = Column(String)
    size = Column(Float)
    format = Column(String)