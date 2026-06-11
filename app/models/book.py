from sqlalchemy import Column, Integer, String

from app.database.connection import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    copies = Column(Integer, nullable=False, default=1)
    status = Column(String, nullable=False, default="Disponível")