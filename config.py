import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = os.getenv("DEBUG")
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Zq4t7w!z%C*F-JaNdRgUjXn2r5u8x/A?D(G+KbPeShVmYp3s6v9y$B&E)H@McQfT'
    POSTGRES = {
        'user': 'postgres',
        'pw': 'postgres',
        'db': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

