import os
from typing import Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем ключ API из переменной окружения
API_KEY: str = os.getenv("API_KEY") or ""

# URL API для получения курсов валют
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/convert"


def returns_transaction_amount(transaction: Dict[str, Dict[str, float]]) -> float:
    amount: float = transaction["operationAmount"]["amount"]
    currency: str = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(amount)

    elif currency in ["USD", "EUR"]:
        params: Dict[str, str] = {"to": "RUB", "from": currency, "amount": str(amount)}
        headers: Dict[str, str] = {"apikey": API_KEY}
        response = requests.get(BASE_URL, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return float(data.get("result", 0))  # Изменено здесь
        else:
            raise Exception("Ошибка получения данных о курсе валют")

    else:
        raise ValueError("Неизвестная валюта")


# Примеры транзакций
transaction_usd: Dict[str, Dict[str, float]] = {"operationAmount": {"amount": 100.0, "currency": {"code": "USD"}}}
transaction_eur: Dict[str, Dict[str, float]] = {"operationAmount": {"amount": 100.0, "currency": {"code": "EUR"}}}
transaction_rub: Dict[str, Dict[str, float]] = {"operationAmount": {"amount": 100.0, "currency": {"code": "RUB"}}}

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
