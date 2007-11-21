import datetime

from sqlalchemy import *

metadata = MetaData()

customer_table = Table('customer', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('firstName', String(20)),
    Column('lastName', String(20)),
    Column('pwd', String(15))
)

category_table = Table('category', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(20)),
    Column('image', String(50))
)

product_table = Table('product', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('category_id', Integer, ForeignKey('category.id')),
    Column('name', String(30)),
    Column('description', String(255), nullable=True),
    Column('image', String(50), nullable=True),
    Column('price', Float)
)

order_table = Table('order', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('customer_id', Integer, ForeignKey('customer.id')),
    Column('status', String(10), default='pending'),
    Column('date', Date, default=datetime.datetime.now)
)

order_item_table = Table('order_item', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('order_id', Integer, ForeignKey('order.id')),
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('price', Float),
    Column('quantity', Integer)
)

def get_engine():
    return create_engine('sqlite://./temp.db')

def create(engine):
    metadata.create_all(bind=engine)
