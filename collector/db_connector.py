from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
db_engine = create_engine('sqlite:///:./db.sqlite', echo=True)
Session = sessionmaker(bind=db_engine)
session_object = Session()

