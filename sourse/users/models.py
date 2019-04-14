from sqlalchemy import Column, String
from sourse.core.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

