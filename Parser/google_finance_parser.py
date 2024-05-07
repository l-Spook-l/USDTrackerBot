import requests
from bs4 import BeautifulSoup


def get_data() -> dict:
    # URL Google Finance
    url = "https://www.google.com/finance/quote/USD-UAH"

    # Page loading.
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Finding the required element.
    currency_div = soup.find("div", {"data-source": True, "data-target": True, "data-last-price": True})
    # Rounding the obtained value.
    rate = round(float(currency_div["data-last-price"]), 4)

    return {
        "Currency_pair": f"{currency_div['data-source']}-{currency_div['data-target']}",
        "Exchange_rate": rate
    }


if __name__ == "__main__":
    get_data()
