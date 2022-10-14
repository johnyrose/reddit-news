from collector import collect_subreddits
from common.db_connector import Base, db_engine

if __name__ == '__main__':
    Base.metadata.create_all(db_engine)
    collect_subreddits()
