import json
import re
from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import numpy as np
import pandas as pd
import requests
import yfinance as yf


def get_greeting(now: Optional[datetime] = None) -> str:
    """Возвращает приветствие в зависимости от текущего времени суток."""
    now = now or datetime.now()
    hour = now.hour
    if 6 <= hour <= 11:
        return "Доброе утро"
    elif 12 <= hour <= 17:
        return "Добрый день"
    elif 18 <= hour <= 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_currency_rates(currencies: List[str]) -> List[Dict[str, Optional[float]]]:
    """Получает актуальные курсы валют по отношению к рублю через внешний API."""
    rates: List[Dict[str, Optional[float]]] = []
    try:
        url = f"https://api.exchangerate.host/latest?base=RUB&symbols={','.join(currencies)}"
        res = requests.get(url, timeout=10)
        data = res.json().get("rates", {})
        for cur in currencies:
            rate = data.get(cur)
            rates.append({"currency": cur, "rate": float(rate) if rate else None})
    except Exception:
        for cur in currencies:
            rates.append({"currency": cur, "rate": None})
    return rates


def get_stock_prices(stocks: List[str]) -> List[Dict[str, Optional[float]]]:
    """Получает текущие биржевые цены указанных акций через Yahoo Finance."""
    result: List[Dict[str, Optional[float]]] = []
    for symbol in stocks:
        try:
            ticker = yf.Ticker(symbol)
            price = ticker.info.get("regularMarketPrice")
            if price and price > 0:
                result.append({"stock": symbol, "price": float(price)})
            else:
                result.append({"stock": symbol, "price": None})
        except Exception:
            result.append({"stock": symbol, "price": None})
    return result


def last_digits(card: Any) -> str:
    """Возвращает последние 4 цифры номера карты."""
    card = str(card)
    m = re.search(r"(\d{4})$", card)
    return m.group() if m else card[-4:]


def to_python_types(obj: Any) -> Any:
    """Рекурсивно приводит все значения numpy-типов к стандартным питоновским (int, float)."""
    if isinstance(obj, dict):
        return {k: to_python_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_python_types(x) for x in obj]
    elif isinstance(obj, (np.integer, np.int64)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float64)):
        return float(obj)
    else:
        return obj


def main() -> None:
    """Главная функция обработки данных — читает файл, формирует итоговый JSON, выводит результат."""
    df = pd.read_excel("data/operations.xlsx")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], errors="coerce", dayfirst=True).dt.strftime("%d.%m.%Y")

    greeting: str = get_greeting()

    df["last_digits"] = df["Номер карты"].apply(last_digits)
    cards: List[Dict[str, Any]] = []
    for digits, group in df.groupby("last_digits"):
        spent = round(float(group[group["Сумма операции"] < 0]["Сумма операции"].sum() * -1), 2)
        cashback = round(float(group["Бонусы (включая кэшбэк)"].sum()), 2)
        cards.append({"last_digits": digits, "total_spent": spent, "cashback": cashback})

    df["amount"] = df["Сумма операции"].astype(float)
    top5 = df.sort_values("amount", ascending=False).head(5)
    top_transactions: List[Dict[str, Any]] = []
    for _, row in top5.iterrows():
        top_transactions.append(
            {
                "date": row["Дата операции"],
                "amount": float(row["amount"]),
                "category": row["Категория"],
                "description": row["Описание"],
                "rounding_to_investbox": float(row["Округление на инвесткопилку"]),
                "rounded_amount": float(row["Сумма операции с округлением"]),
            }
        )

    currencies: List[str] = ["USD", "EUR"]
    stocks: List[str] = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    currency_rates: List[Dict[str, Optional[float]]] = get_currency_rates(currencies)
    stock_prices: List[Dict[str, Optional[float]]] = get_stock_prices(stocks)

    result: Dict[str, Any] = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }
    result = to_python_types(result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()


# python src/views.py
# black src/views.py
# flake8 src/views.py
# mypy src/views.py
# isort src/views.py
