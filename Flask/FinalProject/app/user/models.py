from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer,String
from app.extensions import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str]
    posts: Mapped['Post'] = relationship(back_populates="user")

    def __init__(self,username,password):
        self.username = username
        self.password = password