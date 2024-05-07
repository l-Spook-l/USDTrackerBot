import datetime
import asyncio
import schedule
from config import dp, bot
from utils import update_database


async def check_time():
    print('Start check update database')

    # Scheduling the task to run every hour
    schedule.every().hour.at(":00").do(update_database)

    time_correction = datetime.timedelta(seconds=0)
    while True:
        await asyncio.sleep(60 - time_correction.total_seconds())
        now = datetime.datetime.now()
        schedule.run_pending()
        # Removing the margin of error
        time_correction = datetime.datetime.now() - now


async def start_bot():
    print('Bot online!')
    await dp.start_polling(bot)


async def main():
    tasks = [check_time(), start_bot()]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
