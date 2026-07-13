import json

# переменная json_file_path используется для передачи пути к файлу в функцию в качестве аргумента file_path
json_file_path = "./data/operations.json"


def json_file_returns_list_dictionaries(file_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях."""

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Проверяем, что данные являются списком
            if isinstance(data, list):
                return data
            else:
                return []  # Если данные не являются списком
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Возвращаем пустой список в случае ошибки


print(json_file_returns_list_dictionaries(json_file_path))


# python src/utils.py
# black src/utils.py
# flake8 src/utils.py
# mypy src/utils.py
# isort src/utils.py
