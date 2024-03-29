from sqlalchemy import Column, Integer, String
from common.db_connector import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    score = Column(Integer)  # The upvotes it got on Reddit
    post_id = Column(String)
    subreddit = Column(String)
    title = Column(String)
    text = Column(String)
    url = Column(String)
    image_url = Column(String, nullable=True)
