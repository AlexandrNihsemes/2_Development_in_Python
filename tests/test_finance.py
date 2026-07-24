import unittest
from typing import Dict, List
from unittest.mock import mock_open, patch

import pandas as pd

from src.finance import transactions_csv, transactions_excel_xlsx


def test_transactions_csv() -> None:
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="id;state;date;amount;currency_name;currency_code;"
        "from;to;description\n1;done;2023-01-01;100;USD;USD;"
        "Alice;Bob;Payment for services",
    )
    def inner(mock_file: mock_open) -> None:
        # Вызов функции
        transactions: List[Dict[str, str]] = transactions_csv("./data/transactions.csv")

        # Проверяем, что файл был открыт
        mock_file.assert_called_once_with("./data/transactions.csv", "r", encoding="utf-8")

        # Проверяем, что возвращаемые данные соответствуют ожидаемым
        expected: List[Dict[str, str]] = [
            {
                "id": "1",
                "state": "done",
                "date": "2023-01-01",
                "amount": "100",
                "currency_name": "USD",
                "currency_code": "USD",
                "from": "Alice",
                "to": "Bob",
                "description": "Payment for services",
            }
        ]
        assert transactions == expected

    inner()  # Вызов внутренней функции для выполнения теста


if __name__ == "__main__":
    unittest.main()


def test_transactions_excel_xlsx() -> None:
    # Патчим функцию чтения Excel
    with patch('pandas.read_excel') as mock_read_excel:
        # Создаем фейковые данные для возврата из mock
        dummy_data = {
            'id': ['1'],  # Изменено на строку
            'state': ['done'],
            'date': ['2023-01-01'],
            'amount': ['100'],  # Изменено на строку
            'currency_name': ['USD'],
            'currency_code': ['USD'],
            'from': ['Alice'],
            'to': ['Bob'],
            'description': ['Payment for services']
        }
        mock_read_excel.return_value = pd.DataFrame(dummy_data)  # Возвращаем DataFrame

        # Вызов функции
        transactions: List[Dict[str, str]] = transactions_excel_xlsx('./data/transactions_excel.xlsx')

        # Проверяем, что функция была вызвана с правильным аргументом
        mock_read_excel.assert_called_once_with('./data/transactions_excel.xlsx')

        # Проверяем, что возвращаемые данные соответствуют ожидаемым
        expected: List[Dict[str, str]] = [
            {
                "id": "1",
                "state": "done",
                "date": "2023-01-01",
                "amount": "100",
                "currency_name": "USD",
                "currency_code": "USD",
                "from": "Alice",
                "to": "Bob",
                "description": "Payment for services",
            }
        ]
        assert transactions == expected  # Проверка на равенство

# Запуск теста
if __name__ == '__main__':
    unittest.main()


# python tests/test_finance.py
# black tests/test_finance.py
# flake8 tests/test_finance.py
# mypy tests/test_finance.py
# isort tests/test_finance.py
