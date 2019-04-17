from flask import request, jsonify
from flasgger import SwaggerView
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from sqlalchemy import and_

from sourse.database import db
from sourse.posts.models import Post, Like
from sourse.posts.schemes import LikeSchema, PostSchema


class LikeResource(SwaggerView):

    parameters = LikeSchema
    responses = {
        200: {
            'description': 'A single user',
            'schema': LikeSchema
        }
    }

    @jwt_required
    def post(self):
        data = request.json
        data["user_id"] = get_jwt_identity()

        like, errors = LikeSchema().load(request.json)
        if errors:
            return jsonify(errors), 400

        db.session.add(like)
        db.session.commit()

        return jsonify(LikeSchema().dump(like)), 200


class PostResource(SwaggerView):

    parameters = PostSchema
    responses = {
        200: {
            'description': 'A single user',
            'schema': PostSchema
        }
    }

    @jwt_required
    def post(self):
        print("-----------------------")
        data = request.json
        data["user_id"] = get_jwt_identity()

        post, errors = PostSchema().load(data)
        if errors:
            return jsonify(errors), 400

        db.session.add(post)
        db.session.commit()
        print(post)
        print(post.__dict__)
        print(jsonify(PostSchema().dump(post)).__dict__)
        return jsonify(PostSchema().dump(post)), 200
