from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import Restaurant, Review
from main import Review
from main import Customer

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # session.query().delete()
    session.commit()
    
# tilapiatips = Restaurant(name="Tilapia Tips", price=60)
# mickyds = Restaurant(name="Micky D's", price=30)
# nobu = Restaurant(name="Nobu", price=50)
# grenierpain = Restaurant(name="Le Grenier au Pain", price=62)

# print("New Restaurant alert...")

# session.bulk_save_objects([tilapiatips, mickyds, nobu, grenierpain])
# session.commit()

    # Restaurant.add_restaurant(session, 'Shicken Wangs Place', price=15)
    # Restaurant.add_restaurant(session, 'Rib Shack', price=18)
    # Restaurant.add_restaurant(session, 'ExtraOrdinary Ugali', price=35)
    # Restaurant.add_restaurant(session, 'Poly Nyama Choma', price=12)
    # session.commit()

# Shicken_Wangs_Place = Restaurant(name='Shicken Wangs Place', price=15)
# session.add(Shicken_Wangs_Place)
# session.commit()
# Rib_Shack = Restaurant(name='Rib Shack', price=18)
# session.add(Rib_Shack)
# session.commit()
# Extra_Ordinary_Ugali = Restaurant(name='ExtraOrdinary Ugali', price=35)
# session.add(Extra_Ordinary_Ugali)
# session.commit()
# Poly_Nyama_Choma = Restaurant(name='Poly Nyama Choma', price=12)
# session.add(Poly_Nyama_Choma)
# session.commit()

# restaurant = session.query(Restaurant).all()
# print(restaurant)

# restaurants = [
#     Restaurant(
#         name=fake.name(),
#         price=random.randint(0, 60)
#     )
# for i in range(50)]


# session.bulk_save_objects(restaurants)
# session.commit()