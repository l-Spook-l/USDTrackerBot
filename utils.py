import pandas as pd
import matplotlib.pyplot as plt
from Parser.google_finance_parser import get_data
from DataBase.database_operations import add_data_database


def update_database():
    # Fetching data
    data = get_data()
    # Adding data to the database
    add_data_database(data)
    print('Database updated')


def create_excel_from_db(data):
    # Creating a DataFrame with currency exchange rate data over time
    data_test = {
        'Time': [],
        'Exchange rate': [],
    }

    if data:
        for user_data in data:
            user_settings = user_data[0]
            data_test['Time'].append(user_settings.Timestamp)
            data_test['Exchange rate'].append(user_settings.Exchange_rate)

    df = pd.DataFrame(data_test)

    # Plotting the graph
    plt.figure(figsize=(12, 8))
    plt.plot(df['Time'], df['Exchange rate'], marker='o', label='USD')
    plt.title('Exchange Rates Over Time')
    plt.xlabel('Time')
    plt.ylabel('Exchange Rate')
    plt.legend()
    plt.grid(True)

    # Saving the graph to a file
    plt.savefig('exchange_rates.png')

    # Saving data and graph to Excel using xlsxwriter
    with pd.ExcelWriter("Today's currency exchange rate.xlsx", engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Exchange Rates', index=False)

        # Obtaining a link to the Excel sheet
        worksheet = writer.sheets['Exchange Rates']

        # Inserting the graph image into cell E2.
        worksheet.insert_image('E2', 'exchange_rates.png', {'x_scale': 0.5, 'y_scale': 0.5})


if __name__ == "__main__":
    update_database()
