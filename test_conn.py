from psycopg2 import connect, DatabaseError
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select


metadata = MetaData()
engine = create_engine('postgresql+psycopg2://postgres:567234@localhost/postgres')


users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('email', String, nullable=False)
)


metadata.create_all(engine)

if __name__ == '__main__':
    with engine.connect() as conn:
        new_user = users.insert().values(fullname='Sasha READ')
        result_insert_user = conn.execute(new_user)


        users_select = select(users)
        result = conn.execute(users_select)
        for row in result:
            print(row)

        new_address = addresses.insert().values(email='alex@gmail.com', user_id=1)
        print(new_address)
        result = conn.execute(new_address)

        address_select = select(addresses)
        result = conn.execute(address_select)
        for row in result:
            print(row)
        conn.commit()
        conn.close()