import os

from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from sourse.urls import Router

app = Flask(__name__)
swagger = Swagger(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "Zq4t7w!z%C*F-JaNdRgUjXn2r5u8x/A?D(G+KbPeShVmYp3s6v9y$B&E)H@McQfT"
POSTGRES = {
        'user': 'postgres',
        'pw': 'postgres',
        'db': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
jwt = JWTManager(app)
Router().add_routes(app)
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()