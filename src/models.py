from sqlalchemy import String, ForeignKey, Date, Column, Integer
from database import Base
from sqlalchemy.orm import relationship

from src.orm import create_tables


class Clients(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=150))
    address = Column(String)
    phone = Column(String(length=12))

    orders = relationship('Order', back_populates='client')


class Employees(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=150))
    surname = Column(String(length=150))
    patronymic = Column(String(length=150))
    job_title = Column(String(length=150))
    address = Column(String)
    phone = Column(String(length=12))
    birth_date = Column(Date)

    orders = relationship('Order', back_populates='employee')


class Suppliers(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=150))
    representative = Column(String(length=150))
    contacts = Column(String)
    phone = Column(String(length=12))
    address = Column(String)

    supplies = relationship('Supplies', back_populates='supplier')


class Supplies(Base):
    __tablename__ = 'supplies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    delivery_date = Column(Date)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    supplier = relationship('Suppliers', back_populates='supplies')
    products = relationship('Products', back_populates='supply')


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    supplies_id = Column(Integer, ForeignKey('supplies.id'))
    title = Column(String(length=150))
    description = Column(String)

    supply = relationship('Supplies', back_populates='products')
    orders = relationship('Order', back_populates='product')


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(Date)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))

    employee = relationship('Employees', back_populates='orders')
    product = relationship('Products', back_populates='orders')
    client = relationship('Clients', back_populates='orders')


if __name__ == '__main__':

    create_tables()

    print('Таблицы созданы')
