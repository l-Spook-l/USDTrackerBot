from datetime import date
from sqlalchemy import insert, select, func
from .models import CurrencyRate
from .config_db import session


def add_data_database(data: dict) -> bool:
    try:
        with session() as s:
            stat = insert(CurrencyRate).values(**data)
            s.execute(stat)
            s.commit()
            return True
    except Exception as error:
        print(f"Error occurred while adding data: {error}")
        return False


def get_data_database() -> CurrencyRate | bool:
    try:
        with session() as s:
            query = select(CurrencyRate).filter(func.Date(CurrencyRate.Timestamp) == date.today())
            res = s.execute(query)
            result = res.all()
        return result
    except Exception as error:
        print(f"Error occurred while reading data: {error}")
        return False
