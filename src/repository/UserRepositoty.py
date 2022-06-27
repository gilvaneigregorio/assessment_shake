from typing import TypeVar
from pydantic import BaseModel

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.dao.User import User
from models.dto.User import UserCreate
from core.Security import get_password_hash

def get_one_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create(db: Session, obj_in: UserCreate):
    create_data = obj_in.dict()
    create_data.pop("password")
    db_obj = User(**create_data)
    db_obj.password = get_password_hash(obj_in.password)
    db.add(db_obj)
    db.commit()

    return db_obj