import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy_db.models import *

user = 'postgres'
password = 'localadm'
host = 'localhost'
port = 5432
db = 'olist'
url = 'postgresql://{}:{}@{}:{}/{}'
url = url.format(user, password, host, port, db)

engine = create_engine(url, client_encoding='utf8')
meta = MetaData(bind=engine, reflect=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
#Base = declarative_base()
Base.query = db_session.query_property()


def create_table_phone():
    phone = sqlalchemy.Table('phone', meta,
                             sqlalchemy.Column('number',
                                               sqlalchemy.String,
                                               primary_key=True)
                             )
    meta.create_all(engine)


def create_table_call():
    call = sqlalchemy.Table('call', meta,
                            sqlalchemy.Column('id',
                                              sqlalchemy.Integer,
                                              primary_key=True),
                            sqlalchemy.Column('type_start',
                                              sqlalchemy.Boolean),
                            sqlalchemy.Column('timestamp',
                                              sqlalchemy.TIMESTAMP),
                            sqlalchemy.Column('call_id',
                                              sqlalchemy.Integer),
                            sqlalchemy.Column('source',
                                              sqlalchemy.String,
                                              sqlalchemy.ForeignKey('phone.number')),
                            sqlalchemy.Column('destination',
                                              sqlalchemy.String,
                                              sqlalchemy.ForeignKey('phone.number'))
                            )
    meta.create_all(engine)


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    phone = Phone(number="5514987654321")
    db_session.add(phone)
    phone2 = Phone(number="5514123456789")
    db_session.add(phone2)
    db_session.commit()

    call = Call(type_start = True, call_id=1, source="5514987654321",
                destination="5514123456789")
    db_session.add(call)
    call2 = Call(type_start=False, call_id=1)
    db_session.add(call2)
    db_session.commit()

Phone.__table__
Phone.__mapper__

Call.__table__
Call.__mapper__

Base.metadata.create_all(engine)

#create_table_phone()
#create_table_call()
init_db()