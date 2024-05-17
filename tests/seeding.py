# seeding.py

import factory
from faker import Factory as FakerFactory
from src.resource.authentication.model import User
from factory.faker import Faker
from pytest_factoryboy import register

faker = FakerFactory.create()

@register
class Users_factory(factory.Factory):
    class Meta:
        model = User

    # id = Faker('randome_int')
    name = Faker('name')
    email = Faker('email')
    password = Faker('password')
    dob = Faker('date_of_birth')
    gender = Faker('text')
    bio = Faker('text')
    

