import pandas as pd
import matplotlib.pyplot as plt
from Parser.google_finance_parser import get_data
from DataBase.database_operations import add_data_database


def update_database():
    # Получаем данные
    data = get_data()
    # Добавляем данные в базу данных
    add_data_database(data)
    print('Database updated')


def create_excel_from_db(data):
    # Создание DataFrame с данными о курсе валют относительно времени
    data_test = {
        'Time': [],
        'Exchange rate': [],
    }

    if data:
        for user_data in data:
            # print(r)
            # r += 1
            user_settings = user_data[0]
            data_test['Time'].append(user_settings.Timestamp)
            data_test['Exchange rate'].append(user_settings.Exchange_rate)
            # print(user_settings.Currency_pair)
            # print(user_settings.Exchange_rate)
            # print(user_settings.Timestamp)
            # print('========================')

    df = pd.DataFrame(data_test)

    # Построение графика
    plt.figure(figsize=(12, 8))
    plt.plot(df['Time'], df['Exchange rate'], marker='o', label='USD')
    plt.title('Exchange Rates Over Time')
    plt.xlabel('Time')
    plt.ylabel('Exchange Rate')
    plt.legend()
    plt.grid(True)

    # Сохранение графика в файл
    plt.savefig('exchange_rates.png')

    # Сохранение данных и графика в Excel с использованием xlsxwriter
    with pd.ExcelWriter("Today's currency exchange rate.xlsx", engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Exchange Rates', index=False)

        # Получение ссылки на лист Excel
        worksheet = writer.sheets['Exchange Rates']

        # Вставка изображения графика в ячейку E2
        worksheet.insert_image('E2', 'exchange_rates.png', {'x_scale': 0.5, 'y_scale': 0.5})


if __name__ == "__main__":
    update_database()
