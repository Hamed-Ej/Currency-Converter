import os

import requests
from cachetools import TTLCache, cached

# first define the API_KEY environment variable in your terminal.
API_KEY = os.environ.get("API_KEY")

ttl_cache = TTLCache(maxsize=100, ttl=3 * 60 * 60)


@cached(ttl_cache)
def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["conversion_rates"][target_currency]
    else:
        return None


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


if __name__ == "__main__":
    base_currency = input("Enter your base currency: ")
    target_currency = input("Enter your target currency: ")
    amount = input("Enter amount: ")
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    final_amount = convert_currency(amount, exchange_rate)
    print(f"{amount} {base_currency} is {final_amount} {target_currency}")
