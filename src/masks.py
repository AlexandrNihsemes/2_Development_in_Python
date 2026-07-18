import logging
import os

# Настройка логирования
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)  # Уровень логирования не ниже DEBUG

# Создаем обработчик для записи логов в файл
log_file_path = os.path.join(os.getcwd(), "masks.log")
file_handler = logging.FileHandler(log_file_path, encoding="utf-8")  # Указываем кодировку
file_handler.setLevel(logging.DEBUG)  # Уровень обработчика

# Создаем форматер для логов
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)  # Устанавливаем форматер для обработчика

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX."""

    # Проверяем, что номер карты состоит из 16 цифр и состоит из цифр
    if len(card_number) != 16 or not card_number.isdigit():
        logger.error("Неверный ввод номера карты")  # Логирование ошибки
        raise ValueError("Неверный ввод")

    # Формируем маску
    masked_number = f"{card_number[:6]}******{card_number[12:]}"
    logger.info(f"Замаскированный номер карты: {masked_number}")  # Логирование успешного случая
    # Форматируем номер с пробелами
    return " ".join([masked_number[i : i + 4] for i in range(0, len(masked_number), 4)])


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX."""

    # Проверяем, что номер счета состоит из 20 цифр и состоит из цифр
    if len(account_number) != 20 or not account_number.isdigit():
        logger.error("Неверный ввод номера счета")  # Логирование ошибки
        raise ValueError("Неверный ввод")

    # Формируем маску
    account_mask = "**" + account_number[-4:]
    logger.info(f"Замаскированный номер счета: {account_mask}")  # Логирование успешного случая
    return account_mask


# Примеры использования
if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))  # Ожидается: 700079 ****** 6361
    print(get_mask_account("73654108430135874305"))  # Ожидается: **7305


# python src/masks.py
# black src/masks.py
# flake8 src/masks.py
# mypy src/masks.py
# isort src/masks.py
