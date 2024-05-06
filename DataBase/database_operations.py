from sqlalchemy import insert, select
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



