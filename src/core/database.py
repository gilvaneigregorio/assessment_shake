from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core import environment

async_engine = create_async_engine(environment.DATABASE_URI_ASYNC)
engine = create_engine(environment.DATABASE_URI, connect_args={}, future=True)

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
