from datetime import datetime


def filter_by_state(dictionary_list: list[dict], state: str="EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список,
    содержащий только те словари, у которых ключ state соответствует указанному значению.
    """

    # Создаем пустой список для хранения отфильтрованных словарей
    filtered_list = []

    # Проходим по каждому элементу в исходном списке
    for item in dictionary_list:
        # Проверяем, соответствует ли значение ключа 'state' указанному состоянию
        if item["state"] == state:
            # Если да, добавляем элемент в отфильтрованный список
            filtered_list.append(item)

    # Возвращаем отфильтрованный список
    return filtered_list


def sort_by_date(dictionary_list: list[dict], parameter: bool=True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
    отсортированный по дате (date)."""

    sort_list = sorted(dictionary_list, key=lambda x: x["date"], reverse=parameter)

    # Проверка корректности формата даты
    for item in dictionary_list:
        try:
            # Изменённый формат даты, включающий время
            datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {item['date']}")

    return sort_list


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)

print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
        ]
    )
)

print(
    filter_by_state(
        [
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)


# python src/processing.py
# black src/processing.py
# flake8 src/processing.py
# mypy src/processing.py
# isort src/processing.py
