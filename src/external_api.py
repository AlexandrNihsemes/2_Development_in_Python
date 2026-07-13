import os

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем ключ API из переменной окружения
API_KEY = os.getenv("API_KEY")

# URL API для получения курсов валют
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def returns_transaction_amount(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и
    возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
     для получения текущего курса валют и конвертации суммы операции в рубли.
    """
    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return float(amount)

    elif currency in ["USD", "EUR"]:
        # Формируем URL с динамическими параметрами
        params = {"to": "RUB", "from": currency, "amount": amount}
        headers = {"apikey": API_KEY}
        response = requests.get(BASE_URL, headers=headers, params=params)
        data = response.json()

        if response.status_code == 200:
            # Получаем сумму в рублях из ответа API
            return data.get("result", 0)
        else:
            raise Exception("Ошибка получения данных о курсе валют")

    else:
        raise ValueError("Неизвестная валюта")


# Примеры транзакций
transaction_usd = {"amount": 100, "currency": "USD"}
transaction_eur = {"amount": 100, "currency": "EUR"}
transaction_rub = {"amount": 100, "currency": "RUB"}

try:
    print(returns_transaction_amount(transaction_usd))  # Конвертирует 100 USD в RUB
    print(returns_transaction_amount(transaction_eur))  # Конвертирует 100 EUR в RUB
    print(returns_transaction_amount(transaction_rub))  # Вернет 100 RUB
except Exception as e:
    print(e)


# python src/external_api.py
# black src/external_api.py
# flake8 src/external_api.py
# mypy src/external_api.py
# isort src/external_api.py
