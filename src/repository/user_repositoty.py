from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.dao.user import User
from models.dto.user import UserCreate
from core.security import get_password_hash


async def get_one_by_id(db: AsyncSession, id: str):
    query = select(User).where(User.id == id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_one_by_email(db: AsyncSession, email: str):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def create(db: AsyncSession, obj_in: UserCreate):
    create_data = obj_in.dict()
    create_data.pop("password")
    db_user = User(**create_data)
    db_user.password = get_password_hash(obj_in.password)
    db.add(db_user)
    db.commit()

    return db_user
