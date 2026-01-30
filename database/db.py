from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

engine = create_engine("sqlite:///./data.db")
session = sessionmaker(bind=engine)


def create_table():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_table()
