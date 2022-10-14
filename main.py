from article_generator.generate_articles import generate_articles
from collector import collect_subreddits
from common.db_connector import Base, db_engine, session_object
from models.article import Article

if __name__ == '__main__':
    Base.metadata.create_all(db_engine)
    # collect_subreddits()
    # generate_articles()

    res = session_object.query(Article).all()
    print(res)
