from email.iterators import typed_subpart_iterator

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func

#from sqlalchemy_db.database import *

Base = declarative_base()

class Call(Base):

    __tablename__ = "call"

    id = Column(Integer, primary_key=True)
    type_start = Column(Boolean)

    #func.now() to get the current time when recerd is created
    timestamp = Column(DateTime, default=func.now())

    call_id = Column(Integer)
    source = Column(String, ForeignKey('phone.number'))
    destination = Column(String, ForeignKey('phone.number'))

    def __repr__(self):
        return f"<call('{id}', '{type_start}', '{timestamp}', '{call_id}', '{source}', '{destination}')>" %\
               (self.id, self.type_start, self.timestamp, self.call_id, self.source, self.destination)

class Phone(Base):

    __tablename__ = "phone"

    number = Column(String, primary_key=True)

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"<phone('{number}')>" % (self.number)

    def insert(self, number):
        pass

    def get_all(self):
        pass