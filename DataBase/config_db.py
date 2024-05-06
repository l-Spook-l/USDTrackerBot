from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite:///currency_rates.db"


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(
    url=DATABASE_URL,  # путь к бд
    echo=True,  # логи запроса
)

async_session = async_sessionmaker(async_engine, expire_on_commit=False)
