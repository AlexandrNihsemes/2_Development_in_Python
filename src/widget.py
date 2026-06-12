from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_number):
    """Функция принимает один аргумент - строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером."""

    string_words = account_number.split()

    if "Visa" in string_words or "Maestro" in string_words:
        return " ".join(string_words[0:-1]) + " " + get_mask_card_number(string_words[-1])
    elif "Счет" in string_words[0:-1]:
        return " ".join(string_words[0:-1]) + " " + get_mask_account(string_words[-1])


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date):
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""

    day = date[8:10]
    month = date[5:7]
    year = date[0:4]

    return f"{day}.{month}.{year}"


print(get_date("2024-03-11T02:26:18.671407"))


# python src/widget.py
# black src/widget.py
# flake8 src/widget.py
# mypy src/widget.py
# isort src/widget.py