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



