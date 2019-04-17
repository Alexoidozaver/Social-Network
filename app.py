from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from sourse.urls import Router

app = Flask(__name__)

swagger = Swagger(app)
jwt = JWTManager(app)
Router().add_routes(app)
db = SQLAlchemy(app)

app.config.from_object('config')

if __name__ == '__main__':
    app.run()