import os
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from DataBase.database_operations import get_data_database

from .client_buttons import start_kb

client_router = Router()


@client_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привіт", reply_markup=start_kb)



