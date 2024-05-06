import requests
from bs4 import BeautifulSoup


def get_data() -> dict:
    # URL страницы Google Finance
    url = "https://www.google.com/finance/quote/USD-UAH"

    # Загрузка страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Нахождение нужного элемента
    # currency_div = soup.find("div", {"data-source": "USD", "data-target": "UAH", "data-last-price": "39.25688"})
    currency_div = soup.find("div", {"data-source": True, "data-target": True, "data-last-price": True})

    print(currency_div["data-last-price"], type(currency_div["data-last-price"]))
    rate = round(float(currency_div["data-last-price"]), 4)
    print(rate)
    print(currency_div["data-source"])
    print(currency_div["data-target"])

    return {
        "Currency_pair": f"{currency_div['data-source']}-{currency_div['data-target']}",
        "Exchange_rate": rate
    }


if __name__ == "__main__":
    print(get_data())
