def get_mask_card_number(card_number):
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX."""

    # Проверяем, что номер карты состоит из 16 цифр
    if len(card_number) != 16:
        raise ValueError("Неверный ввод")
    # Проверяем, что номер карты состоит из цифр
    elif not card_number.isdigit():
        raise ValueError("Неверный ввод")

    first_slice = card_number[:6]  # первый срез до маски
    second_slice = card_number[6:12]  # второй срез - маска
    third_slice = card_number[12:]  # третий срез после маски

    sum_of_cuts = first_slice + "******" + third_slice  # сумма срезов

    slice_1 = sum_of_cuts[:4]  # первый срез
    slice_2 = sum_of_cuts[4:8]  # второй срез
    slice_3 = sum_of_cuts[8:12]  # третий срез
    slice_4 = sum_of_cuts[12:]  # четвёртый срез

    number_with_spaces = (
        slice_1 + " " + slice_2 + " " + slice_3 + " " + slice_4
    )  # номер с пробелами

    return number_with_spaces


def get_mask_account(account_number):
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX."""

    # Проверяем, что номер карты состоит из 20 цифр
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Неверный ввод")
    # Проверяем, что номер карты состоит из цифр
    elif not account_number.isdigit():
        raise ValueError("Неверный ввод")

    slice_account = account_number[-4:]  # срез последних 4-х цифр

    account_mask = "**" + slice_account  # номер с маской

    return account_mask


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))


# python src/masks.py
# flake8 src/masks.py
# mypy src/masks.py
# black src/masks.py
# isort src/masks.py