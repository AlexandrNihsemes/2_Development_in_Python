import re
from collections import Counter
from typing import Dict
from typing import List


def search_transactions(transactions: List[Dict[str, str]], search_term: str) -> List[Dict[str, str]]:
    """Функция для поиска транзакций по заданному слову."""

    pattern = re.compile(search_term, re.IGNORECASE)  # Паттерн для поиска слова в строке
    matching_transactions = []  # Список для хранения подходящих транзакций

    for transaction in transactions:
        value = transaction.get("description", "")
        if isinstance(value, str):  # Проверяем, является ли значение строкой
            if pattern.search(value):
                matching_transactions.append(transaction)

    return matching_transactions


# Тест
if __name__ == "__main__":
    transactions_list = [
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215",
        },
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472",
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {"amount": "77751.04", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493",
        },
    ]

    search_term = input("Введите слово для поиска: ").strip()
    matching_transactions = search_transactions(transactions_list, search_term)
    print(matching_transactions)  # Выводит список транзакций, соответствующих шаблону


def count_transactions_by_category(transactions: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """Функция для подсчета количества операций по категориям из списка транзакций."""

    descriptions = []
    for tr in transactions:
        descriptions.append(tr.get("description", "Без категории"))
    return Counter(descriptions)


if __name__ == "__main__":
    transactions_list = [
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215",
        },
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472",
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {"amount": "77751.04", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493",
        },
    ]

    categories_list = ["Открытие вклада", "Перевод организации", "Перевод с карты на счет"]
    results = count_transactions_by_category(transactions_list, categories_list)
    print(results)  # Выводит количество операций по категориям


# python src/search.py
# black src/search.py
# flake8 src/search.py
# mypy src/search.py
# isort src/search.py
