from flask import request, jsonify
from flasgger import SwaggerView
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from sqlalchemy import and_

from sourse.database import db
from sourse.users.models import User
from sourse.users.schemes import UserRegistrationSchema, UserAuthenticationSchema


class UserRegistrationResource(SwaggerView):

    parameters = UserRegistrationSchema
    responses = {
        201: {
            'AuthToken': 'A single user',
        }
    }

    def post(self):
        user, errors = UserRegistrationSchema().load(request.json)
        if errors:
            return errors, 400

        if User.query.filter(User.email == request.json["email"]).all():
            return "Email already in use", 400

        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 201


class UserAuthenticationResource(SwaggerView):

    parameters = UserAuthenticationSchema
    responses = {
        201: {
            'AuthToken': 'A single user',
        }
    }

    def post(self):
        """
        User Auth
        """
        _, errors = UserAuthenticationSchema().load(request.json)
        if errors:
            return errors, 400

        user = User.query.filter(
            and_(
                User.email == request.json["email"],
                User.password == request.json["password"],
            )).one()

        if not user:
            return "Wrong email or password", 400
        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 201
