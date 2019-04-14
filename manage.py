from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from sourse.database import db
from config import Config
from sourse.posts.models import Post, Like
from sourse.users.models import User

app.config.from_object(Config())
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()