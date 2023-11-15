from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from factories import create_fake_person

from config import settings


engine = create_engine(
    settings.sync_database_url,
    echo=settings.db_echo_log,
)

async_engine = create_async_engine(
    settings.async_database_url,
    echo=settings.db_echo_log,
    future=True,
)

async_session = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


async def create_db_and_tables() -> None:
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


async def bulk_create_profiles(number: int) -> None:
    async with AsyncSession(async_engine) as session:
        for _ in range(number):
            person = create_fake_person()
            session.add(person)
        await session.commit()
