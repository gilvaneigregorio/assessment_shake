from sqlalchemy import Integer, String, Column
from core.Database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)
