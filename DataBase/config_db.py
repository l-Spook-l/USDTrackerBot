from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///currency_rates.db"


class Base(DeclarativeBase):
    pass


engine = create_engine(
    url=DATABASE_URL,
    echo=False,
)

session = sessionmaker(engine, expire_on_commit=False)
