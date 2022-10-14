from sqlalchemy import Column, Integer, String, Boolean
from common.db_connector import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    article_id = Column(String)
    text = Column(String)
    url = Column(String)
    image_url = Column(String, nullable=True)
