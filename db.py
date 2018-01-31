import sqlalchemy


class database():

    def connect(self, user, password, db, host='localhost', port=5432):
        '''Returns a connection and a metadata object'''

        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)
        con = sqlalchemy.create_engine(url, client_encoding='utf8')
        meta = sqlalchemy.MetaData(bind=con, reflect=True)

        return con, meta

    def create_table_phone(self, con, meta):

            phone = sqlalchemy.Table('phone', meta,
                                     sqlalchemy.Column('number',
                                                       sqlalchemy.String,
                                                       primary_key=True)
                                     )
            meta.create_all(con)

    def create_table_call(self, con, meta):

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
        meta.create_all(con)

db = database()
con, meta = db.connect('postgres','localadm','olist')
#db.create_table_phone(con, meta)
#db.create_table_call(con, meta)



