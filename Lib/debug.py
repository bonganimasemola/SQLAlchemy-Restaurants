fake = Faker()

fake.name()
fake.price()
fake.name()
fake.price()
fake.name()
fake.price()




restaurants = [
    Restaurants(
        title=fake.name(),
        price=random.randint(0, 60)
    )
for i in range(50)]

session.bulk_save_objects(games)
session.commit()