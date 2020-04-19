from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import DateTime

engine = create_engine('sqlite:////tmp/photos.db', echo=True)
Base = declarative_base(bind=engine)

def get_session():
    Base.metadata.create_all()
    Session = sessionmaker(bind=engine)
    return Session()

class DbPhoto(Base):
    __tablename__ = 'photos'
    unique_id = Column(String, primary_key=True)
    photo_id = Column(String, nullable=True)
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)

    def __init__(self, unique_id, photo_id, width, height):
        self.unique_id = unique_id
        self.photo_id = photo_id
        self.width = width
        self.height = height