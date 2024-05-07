import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()
from Bot.client import client_router

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(client_router)
