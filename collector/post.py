from sqlalchemy import Column, Integer, String, Boolean
from db_connector import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    score = Column(Integer)
    url = Column(String)
    permalink = Column(String)
    image_url = Column(String, nullable=True)
    over_18 = Column(Boolean)
