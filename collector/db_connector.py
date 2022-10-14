from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from collector.settings import DB_FILE

Base = declarative_base()
db_engine = create_engine(f'sqlite:///{DB_FILE}', echo=True)
Session = sessionmaker(bind=db_engine)
session_object = Session()

