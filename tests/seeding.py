# seeding.py

import datetime
import random
import factory
from faker import Factory as FakerFactory
from src.resource.post.model import Posts
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
    otp = factory.Sequence(lambda n: f'{n:06d}') 
    expiration_time = factory.LazyFunction(lambda: datetime.datetime.utcnow())


@register
class Posts_Factory(factory.Factory):
    class Meta:
        model = Posts

    post = Faker('sentence')
    caption = Faker('sentence')
    total_like = random.randint(0, 100)
    uid = factory.SubFactory(Users_factory)
    is_active = True
    is_deleted = False
    created_at = factory.LazyFunction(datetime.datetime.now)
    updated_at = factory.LazyFunction(datetime.datetime.now)
    

