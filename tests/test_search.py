import unittest
from src.search import search_transactions, count_transactions_by_category

# Подготовка данных для тестов
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
]

# Тест функции поиска транзакций


def test_search_transactions_found():
    result = search_transactions(transactions_list, "вклада")
    assert len(result) == 1  # Ожидаем 1 совпадение
    assert result[0]["description"] == "Открытие вклада"


def test_search_transactions_not_found():
    result = search_transactions(transactions_list, "неизвестный")
    assert len(result) == 0  # Ожидаем 0 совпадений


# Тест функции подсчета операций по категориям


def test_count_transactions_by_category():
    categories = ["Открытие вклада", "Перевод организации", "Перевод с карты на счет"]  # Добавляем новую категорию
    result = count_transactions_by_category(transactions_list, categories)
    assert result["Открытие вклада"] == 1  # 1 операция в категории
    assert result["Перевод организации"] == 1  # 1 операция в категории
    assert result["Перевод с карты на счет"] == 0  # 0 операций в категории


# Запуск тестов
if __name__ == "__main__":
    test_search_transactions_found()
    test_search_transactions_not_found()
    test_count_transactions_by_category()
    print("Все тесты пройдены успешно!")


# black tests/test_search.py
