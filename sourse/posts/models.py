from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sourse.core.models import BaseModel


class Post(BaseModel):
    __tablename__ = 'posts'
    text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")


class Like(BaseModel):
    __tablename__ = 'likes'
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))