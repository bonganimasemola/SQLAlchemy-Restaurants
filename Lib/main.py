

from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())
    #reviews = relationship('Review', back_populates='restaurant')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Restaurant: {self.name}, ' \
               + f'{self.price} dollars'
               
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    # reviews = relationship('Review', back_populates='customer')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Customer: {self.name}'
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    restaurant_id = Column(Integer())
    customer_id = Column(Integer())
    # restaurant = relationship('Restaurant', back_populates='reviews')
    # customer = relationship('Customer', back_populates='reviews')

    def __init__(self, star_rating, restaurant, customer):
        self.star_rating = star_rating
        self.restaurant = restaurant
        self.customer = customer
    
    
    
    
    
if __name__ == '__main__':
    # engine = create_engine('sqlite:///migrations_test.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    # restaurant = Restaurant('Shicken Wangs Place')
    # session.add(restaurant)
    # session.commit()
    
    Shicken_Wangs_Place = Restaurant(name='Shicken Wangs Place', price=15)
    session.add(Shicken_Wangs_Place)
    session.commit()
    Rib_Shack = Restaurant(name='Rib Shack', price=18)
    session.add(Rib_Shack)
    session.commit()
    Extra_Ordinary_Ugali = Restaurant(name='ExtraOrdinary Ugali', price=35)
    session.add(Extra_Ordinary_Ugali)
    session.commit()
    Poly_Nyama_Choma = Restaurant(name='Poly Nyama Choma', price=12)
    session.add(Poly_Nyama_Choma)
    session.commit()
    
    restaurant = session.query(Restaurant).all()
    print(restaurant)
    
    John_Mbaru = Customer(name='John Mbaru')
    session.add(John_Mbaru)
    session.commit()
    Wangachi = Customer(name='Wangachi')
    session.add(Wangachi)
    session.commit()
    Mwangi_Ace = Customer(name='Mwangi Ace')
    session.add(Mwangi_Ace)
    session.commit()
    Sankofa_King = Customer(name='Sankofa King')
    session.add(Sankofa_King)
    session.commit()
    Sean_Carter = Customer(name='Sean Carter')
    session.add(Sean_Carter)
    session.commit()
    Kendrick_Lamar = Customer(name='Kendrick Lamar')
    session.add(Kendrick_Lamar)
    session.commit()
    
    customers = session.query(Customer).all()
    print(customers)