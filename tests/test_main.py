import builtins
from unittest.mock import patch

import pytest

from main import main


def test_main_flow(monkeypatch):
    # Последовательность ответов на input() в main
    inputs = iter(
        [
            "1",  # выбрать JSON
            "EXECUTED",  # статус
            "да",  # сортировка по дате
            "по убыванию",  # по убыванию
            "да",  # только рублевые
            "нет",  # не фильтровать по слову
        ]
    )
    monkeypatch.setattr(builtins, "input", lambda *args: next(inputs))

    # Мокаем все функции, которые работают с файлами или внешними источниками
    with patch(
        "src.utils.json_file_returns_list_dictionaries",
        return_value=[
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-01-01",
                "operationAmount": {"currency": {"code": "RUB"}, "amount": 100},
                "description": "test",
                "to": "1234567890123456",
            }
        ],
    ), patch("src.finance.transactions_csv", return_value=[]), patch(
        "src.finance.transactions_excel_xlsx", return_value=[]
    ), patch(
        "src.generators.filter_by_currency",
        side_effect=lambda lst, code: (x for x in lst if x["operationAmount"]["currency"]["code"] == code),
    ), patch(
        "src.processing.filter_by_state", side_effect=lambda lst, state: [x for x in lst if x["state"] == state]
    ), patch(
        "src.processing.sort_by_date", side_effect=lambda lst, parameter: lst
    ), patch(
        "src.search.search_transactions", side_effect=lambda transactions, search_term: transactions
    ), patch(
        "src.widget.get_date", return_value="01.01.2023"
    ), patch(
        "src.widget.mask_account_card", return_value="**** 3456"
    ):
        # Мокаем print, чтобы не засорять вывод
        with patch("builtins.print") as mock_print:
            result = main()
            # Проверяем, что были вызовы print с ожидаемыми строками
            calls = [call.args[0] if call.args else "" for call in mock_print.call_args_list]
            assert any("Всего банковских операций" in str(c) for c in calls)


# python tests/test_main.py
# black tests/test_main.py
# flake8 tests/test_main.py
# mypy tests/test_main.py
# isort tests/test_main.py
