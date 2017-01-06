from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model_seed import seed_db  
from datetime import datetime

# Base instance for all models
Base = declarative_base()

# create schema for model
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    delivery = Column(String(80))
    free_porto = Column(Boolean(0))
    img_url = Column(String(250))
    kid_adult = Column(Boolean(0))
    kids = Column(Boolean(0))
    name = Column(String(250))
    package = Column(Boolean(0))
    price = Column(String(80))
    price_old = Column(String(0))
    sizes = Column(String(250))
    url = Column(String(250))
    women = Column(Boolean(0))

    # convert sqlalchemy object to dictionary
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# init database
def init_db():
    engine = create_engine('sqlite:///storage/sample.db')
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    #seed database
    seed_db(session, Product)
