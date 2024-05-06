from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from .config_db import Base


class CurrencyRate(Base):
    __tablename__ = 'currency_rate_table'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Currency_pair: Mapped[str] = mapped_column(nullable=False)
    Exchange_rate: Mapped[float]
    Timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow())





