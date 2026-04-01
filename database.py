from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///my_database.db', echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_session():
    return SessionLocal()

session = get_session()
Base.metadata.create_all(engine)