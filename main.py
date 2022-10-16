from article_generator.generate_articles import generate_articles
from collector import collect_subreddits
from common.db_connector import Base, db_engine, session_object
from models.article import Article
from site_generator.generate_site import generate_site

if __name__ == '__main__':
    Base.metadata.create_all(db_engine)
    # collect_subreddits()
    # generate_articles()
    generate_site()
