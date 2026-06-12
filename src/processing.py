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






