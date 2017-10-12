from mongoengine import *
from faker import Faker


class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()

def dump_data():
    f = Faker()
    for _ in range (10):
        girl_type = GirlType(name=f.name(), image="https://via.placeholder.com/400x200", description=f.text())
        girl_type.save()
