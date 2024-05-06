import asyncio
import datetime
from config import dp, bot


async def check_update_database():
    print('Start check exchange rate')
    time_correction = datetime.timedelta(seconds=0)  # Инициализация коррекции времени
    while True:
        await asyncio.sleep(10 - time_correction.total_seconds())  # Ожидание 10 секунд с учетом коррекции времени
        now = datetime.datetime.now()
        print('=================Time now: ', datetime.datetime.now(), '===================================')
        time_correction = datetime.datetime.now() - now
        print(f'###################### Uncertainty - {time_correction.total_seconds()} ###############################')


async def start_bot():
    print('Bot online!')
    await dp.start_polling(bot)  # Запуск бота


async def run_bot():
    tasks = [check_update_database(), start_bot()]  # Задачи для параллельного выполнения
    await asyncio.gather(*tasks)  # ожидает завершения всех задач из списка tasks.
    # Это позволяет выполнить обе задачи параллельно и подождать, пока они завершатся.


if __name__ == "__main__":
    try:
        asyncio.run(run_bot())  # Запуск основной программы
    except KeyboardInterrupt:
        print("Exit")  # Вывод сообщения при прерывании программы пользователем
