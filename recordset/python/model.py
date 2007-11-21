from sqlalchemy.orm import mapper, relation, sessionmaker

from pyamf import register_class

import db

Session = sessionmaker(bind=db.get_engine(), autoflush=True,
    transactional=True)

class Customer(object):
    pass

class Category(object):
    pass

class Product(object):
    pass

class Order(object):
    pass

class OrderItem(object):
    pass

# SQLAlchemy Mappings
mapper(Customer, db.customer_table, properties={
    'orders': relation(Order, backref='customer')
})
mapper(Category, db.category_table)
mapper(Product, db.product_table, properties={
    'categories': relation(Category, backref='product')
})
mapper(OrderItem, db.order_item_table, properties={
    'product': relation(Product)
})
mapper(Order, db.order_table, properties={
    'items': relation(OrderItem, backref='order')
})
