from marshmallow import Schema, fields, post_load

from sourse.users.models import User


class UserRegistrationSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)

    class Meta():
        __model__ = User

    @post_load
    def make_user(self, data):
        return User(**data)


class UserAuthenticationSchema(Schema):
    password = fields.Str(required=True)
    email = fields.Email(required=True)

    class Meta():
        __model__ = User


