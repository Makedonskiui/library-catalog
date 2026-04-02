from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)
    is_read = Column(Boolean, default=False)