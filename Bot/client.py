import os
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from DataBase.database_operations import get_data_database
from utils import create_excel_from_db
from .client_buttons import start_kb

client_router = Router()


@client_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Вітаю! Для отримання інформації про динаміку курсу долара до гривні, "
                         "ви можете ввести команду - /get_exchange_rate, або натиснути кнопку - Get exchange rate",
                         reply_markup=start_kb)


@client_router.message(Command('get_exchange_rate'))
@client_router.message(F.text.lower() == 'get exchange rate')
async def get_exchange_rate(message: Message):
    data = get_data_database()
    create_excel_from_db(data)

    # Получаем текущий рабочий каталог
    current_directory = os.getcwd()

    # Путь к файлу для отправки
    file_path = os.path.join(current_directory, "Today's currency exchange rate.xlsx")

    await message.reply_document(
        document=FSInputFile(path=file_path)
    )
