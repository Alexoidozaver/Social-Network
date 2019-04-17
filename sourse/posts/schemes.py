from marshmallow import Schema, fields, post_load, validates_schema, ValidationError
from sqlalchemy import and_

from sourse.posts.models import Post, Like
from sourse.users.models import User


class LikeSchema(Schema):
    id = fields.Int(read_only=True)
    user_id = fields.Int(required=True)
    post_id = fields.Int(required=True)

    class Meta():
        __model__ = Like

    @validates_schema
    def validate_ids(self, data):
        error = ""
        if not Post.query.filter(Post.id == data["post_id"]).all():
            error += "post_id: No such post, "
        if not User.query.filter(User.id == data["user_id"]).all():
            error += "user_id: No such user, "
        if Like.query.filter(
                and_(
                    Like.post_id == data["post_id"],
                    Like.user_id == data["user_id"]
                )
        ).all():
            error += "like already exist, "
        if error:
            raise ValidationError(error[:-2]+".")

    @post_load
    def make_object(self, data):
        return Like(**data)


class PostSchema(Schema):
    id = fields.Int(read_only=True)
    user_id = fields.Int(required=True)
    text = fields.Str(required=True)

    class Meta():
        __model__ = Post

    @post_load
    def make_object(self, data):
        return Post(**data)

    @validates_schema
    def validate_ids(self, data):
        if not User.query.filter(User.id == data["user_id"]).all():
            raise ValidationError("user_id: No such user.")
