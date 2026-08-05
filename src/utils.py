import json
import logging
import os

# Настройка логирования
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Уровень логирования не ниже DEBUG

# Создаем обработчик для записи логов в файл
log_file_path = os.path.join(os.getcwd(), "utils.log")
file_handler = logging.FileHandler(log_file_path, encoding="utf-8")  # Указываем кодировку
file_handler.setLevel(logging.DEBUG)  # Уровень обработчика

# Создаем форматер для логов
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)  # Устанавливаем форматер для обработчика

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)

# Путь к JSON-файлу
json_file_path = "C:/Users/Did-Fil/PycharmProjects/9.1 Masking bank card and account numbers/data/operations.json"


def json_file_returns_list_dictionaries(file_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях."""
    logger.debug(f"Попытка загрузить данные из файла: {file_path}")  # Логирование успешного случая

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Проверяем, что данные являются списком
            if isinstance(data, list):
                logger.info(f"Данные успешно загружены: {data}")  # Логирование успешного результата
                return data
            else:
                logger.warning("Данные не являются списком")  # Логирование предупреждения
                return []  # Если данные не являются списком
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")  # Логирование ошибки
        return []  # Возвращаем пустой список в случае ошибки
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON")  # Логирование ошибки
        return []  # Возвращаем пустой список в случае ошибки


if __name__ == "__main__":
    print(json_file_returns_list_dictionaries(json_file_path))


# python src/utils.py
# black src/utils.py
# flake8 src/utils.py
# mypy src/utils.py
# isort src/utils.py
