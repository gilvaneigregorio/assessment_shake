from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core import Env

SQLALCHEMY_DATABASE_URL = 'sqlite:///'+Env.DATABASE_URI
ASYNC_SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///'+Env.DATABASE_URI

async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)

AsyncSessionLocal = sessionmaker(
    async_engine, class_ =AsyncSession, expire_on_commit=False
)
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
