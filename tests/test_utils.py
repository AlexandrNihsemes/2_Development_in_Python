import unittest
from unittest.mock import mock_open, patch

from src.utils import json_file_returns_list_dictionaries


# Тест для корректного JSON-файла
@patch("src.utils.open", new_callable=mock_open, read_data='[ {"id": 1, "amount": 100}, {"id": 2, "amount": 200} ]')
def test_valid_json_file(mock_file):
    result = json_file_returns_list_dictionaries("./data/operations.json")
    expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    assert result == expected


# Тест для случая, когда файл не найден
@patch("src.utils.open", new_callable=mock_open)
def test_file_not_found(mock_file):
    mock_file.side_effect = FileNotFoundError
    result = json_file_returns_list_dictionaries("./data/operations.json")
    assert result == []  # Ожидаем пустой список


# Тест для ошибки декодирования JSON
@patch("src.utils.open", new_callable=mock_open, read_data="not a json")
def test_json_decode_error(mock_file):
    result = json_file_returns_list_dictionaries("./data/operations.json")
    assert result == []  # Ожидаем пустой список


# Тест для случая, когда данные не являются списком
@patch("src.utils.open", new_callable=mock_open, read_data='{"id": 1}')
def test_non_list_data(mock_file):
    result = json_file_returns_list_dictionaries("./data/operations.json")
    assert result == []  # Ожидаем пустой список


# Запуск тестов
if __name__ == "__main__":
    unittest.main()


# python tests/test_utils.py
# black tests/test_utils.py
# flake8 tests/test_utils.py
# mypy tests/test_utils.py
# isort tests/test_utils.py