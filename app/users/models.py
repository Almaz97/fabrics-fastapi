from app.core.db import Base
from sqlalchemy import Column, String, Integer, DateTime
import datetime
import bcrypt


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    full_name = Column(String(100))
    email = Column(String(50), unique=True)
    password = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def set_password(self, password):
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())

    def __str__(self):
        return self.username
