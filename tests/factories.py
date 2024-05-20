import factory
from faker import Factory as FakerFactory
from src.resource.post.model import Posts
from src.resource.like.model import Like
from src.resource.follow.model import Follower
from src.resource.comment.model import Post_comment
from src.resource.authentication.model import User, Otp
from pytest_factoryboy import register




faker = FakerFactory.create()

@register
class Users_factory(factory.Factory):
    class Meta:
        model = User


@register
class Otps_Factory(factory.Factory):
    class Meta:
        model = Otp

@register
class Posts_Factory(factory.Factory):
    class Meta:
        model = Posts

@register
class Likes_Factory(factory.Factory):
    class Meta:
        model = Like
@register
class Followers_Factory(factory.Factory):
    class Meta:
        model = Follower
@register
class Comments_Factory(factory.Factory):
    class Meta:
        model = Post_comment