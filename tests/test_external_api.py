import unittest
from unittest.mock import patch

from src.external_api import returns_transaction_amount


# Тестирование конвертации USD
@patch("src.external_api.requests.get")  # Замена requests.get на мок
def test_returns_transaction_amount_usd(mock_get):
    # Настройка мока для ответа от API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: {"result": 7500}  # Предположим, что 100 USD = 7500 RUB

    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
    result = returns_transaction_amount(transaction)
    assert result == 7500


# Тестирование конвертации EUR
@patch("src.external_api.requests.get")  # Замена requests.get на мок
def test_returns_transaction_amount_eur(mock_get):
    # Настройка мока для ответа от API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: {"result": 8000}  # Предположим, что 100 EUR = 8000 RUB

    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "EUR"}}}
    result = returns_transaction_amount(transaction)
    assert result == 8000


# Тестирование суммы в рублях
def test_returns_transaction_amount_rub():
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}
    result = returns_transaction_amount(transaction)
    assert result == 100  # Просто возвращаем сумму


# Тестирование неизвестной валюты
@patch("src.external_api.requests.get")  # Замена requests.get на мок
def test_returns_transaction_amount_invalid_currency(mock_get):
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "GBP"}}}
    try:
        returns_transaction_amount(transaction)
    except ValueError as e:
        assert str(e) == "Неизвестная валюта"


# Тестирование ошибки API
@patch("src.external_api.requests.get")  # Замена requests.get на мок
def test_returns_transaction_amount_api_error(mock_get):
    # Настройка мока для ответа от API с ошибкой
    mock_get.return_value.status_code = 400
    mock_get.return_value.json = lambda: {"error": {"info": "Invalid API key"}}

    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
    try:
        returns_transaction_amount(transaction)
    except Exception as e:
        assert "Ошибка получения данных о курсе валют" in str(e)


# Запуск тестов
if __name__ == "__main__":
    unittest.main()


# python tests/test_external_api.py
# black tests/test_external_api.py
# flake8 tests/test_external_api.py
# mypy tests/test_external_api.py
# isort tests/test_external_api.py
