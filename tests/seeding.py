# seeding.py

import datetime
import factory
from faker import Factory as FakerFactory
from src.resource.authentication.model import User, Otp
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

@register
class Otps_Factory(factory.Factory):
    class Meta:
        model = Otp

        
    email = factory.Faker('email')
    otp = factory.Sequence(lambda n: f'{n:06d}')  # Generates a 6-digit OTP
    expiration_time = factory.LazyFunction(lambda: datetime.datetime.utcnow())
    

