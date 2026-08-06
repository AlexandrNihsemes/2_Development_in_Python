from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> str:
    """Функция принимает один аргумент - строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером."""

    string_words = string.split()

    news_string_words = " ".join(string_words[:-1])

    words_an = ["Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold",  "МИР"]
    words_ru = ["Счет"]

    if news_string_words in words_an and len(string_words[-1]) == 16:
        return news_string_words + " " + get_mask_card_number(string_words[-1])

    elif news_string_words in words_ru and len(string_words[-1]) == 20:
        return news_string_words + " " + get_mask_account(string_words[-1])

    else:
        raise ValueError("Неверный ввод")


# print(mask_account_card("Visa Platinum 7000792289606361"))
# print(mask_account_card("Maestro 7000792289606361"))
# print(mask_account_card("Счет 73654108430135874305"))


def get_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""

    day = date[8:10]
    month = date[5:7]
    year = date[0:4]

    if len(date) != 26:
        raise ValueError("Неверный ввод")
    if int(day) > 31 or int(month) > 12 or int(year) > 2026:
        raise ValueError("Неверный ввод")
    if int(day) == 0 or int(month) == 0 or int(year) == 0:
        raise ValueError("Неверный ввод")

    return f"{day}.{month}.{year}"


# print(get_date("2024-03-11T02:26:18.671407"))


# python src/widget.py
# black src/widget.py
# flake8 src/widget.py
# mypy src/widget.py
# isort src/widget.py
