from flask import request, jsonify
from flasgger import SwaggerView
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from sqlalchemy import and_

from sourse.database import db
from sourse.posts.models import Post, Like


class LikeResource(SwaggerView):

    parameters = LikeSchema
    responses = {
        200: {
            'description': 'A single user',
            'schema': LikeSchema
        }
    }

    def post(self):

        like, errors = LikeSchema().load(request.json)
        if errors:
            return errors, 400

        db.session.add(like)
        db.session.commit()

        return "Like created", 200

    def delete(self, resource_id):

        Like.query.filter(Like.id == resource_id).delete()

        return 200