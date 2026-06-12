def filter_by_state(dictionary_list: list, state="EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED' и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению.)"""

    executed_list = []  # Список для хранения словарей с состоянием EXECUTED
    canceled_list = []  # Список для хранения словарей с состоянием CANCELED

    for item in dictionary_list:

        if item["state"] == state:
            executed_list.append(item)
        elif item["state"] == "CANCELED":
            canceled_list.append(item)

    return executed_list, canceled_list


def sort_by_date(dictionary_list: list, parameter=True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
    отсортированный по дате (date)."""

    sort_list = sorted(dictionary_list, key=lambda x: x["date"], reverse=parameter)

    return sort_list






