from common.db_connector import Base, db_engine
from site_generator.generate_site import generate_site

if __name__ == '__main__':
    Base.metadata.create_all(db_engine)
    # collect_subreddits()
    # generate_articles()
    generate_site()
