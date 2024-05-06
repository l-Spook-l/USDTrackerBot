from aiogram.types import Message
from config import dp
from aiogram.filters import CommandStart


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привіт")

