from src.finance import transactions_csv
from src.finance import transactions_excel_xlsx
from src.generators import filter_by_currency
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.search import search_transactions
from src.utils import json_file_returns_list_dictionaries
from src.widget import get_date
from src.widget import mask_account_card


def main() -> list[dict]:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой."""

    print()
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:  # Цикл для повторного запуска программы
        print("""
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")
        print()

        user = input()
        print()

        if user == "1":
            transactions = json_file_returns_list_dictionaries(
                file_path="C:/Users/Did-Fil/PycharmProjects/"
                "9.1 Masking bank card and account numbers/data/operations.json"
            )
            print("Для обработки выбран JSON-файл.")
            break
        elif user == "2":
            transactions = transactions_csv(
                file_transactions_csv="C:/Users/Did-Fil/PycharmProjects/"
                "9.1 Masking bank card and account numbers/data/transactions.csv"
            )
            print("Для обработки выбран CSV-файл.")
            break
        elif user == "3":
            transactions = transactions_excel_xlsx(
                file_transactions_excel_xlsx="C:/Users/Did-Fil/PycharmProjects/"
                "9.1 Masking bank card and account numbers/data/transactions_excel.xlsx"
            )
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Неверный ввод.")
            continue  # Возвращаемся к началу цикла
    print()

    print(transactions)
    print()

    # Фильтрация по статусу
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        print()
        status = input().strip().upper()

        if status in {"EXECUTED", "CANCELED", "PENDING"}:
            filtration = filter_by_state(transactions, state=status)
            if not filtration:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                return
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f"Статус операции {status} недоступен. Попробуйте снова.")

    filtration = filter_by_state(transactions, state=status)

    print(filtration)
    print()

    while True:
        print("Отсортировать операции по дате? (Да/Нет)")
        print()
        sort_choice = input().strip().lower()

        if sort_choice == "да":
            print("Отсортировать по возрастанию или по убыванию? (По возрастанию/По убыванию)")
            print()
            sort_type = input().strip().lower()

            while True:
                if sort_type == "по возрастанию":
                    filtration_by_state = sort_by_date(dictionary_list=filtration, parameter=False)
                    print("Операции отсортированы по возрастанию даты.")
                    print()
                    break  # Выход из цикла

                elif sort_type == "по убыванию":
                    filtration_by_state = sort_by_date(dictionary_list=filtration, parameter=True)
                    print("Операции отсортированы по убыванию даты.")
                    print()
                    break  # Выход из цикла

                else:
                    print("Неверный выбор сортировки. Букв не видишь, что-ли?")
                    print()
                    sort_type = input().strip().lower()  # Повторный ввод
            break

        elif sort_choice == "нет":
            print("Список будет выведен без сорртировки по возрастанию или по убыванию.")
            print()
            filtration_by_state = filtration
            break
        else:
            print("Неверный ввод. Попробуйте снова I-(")
            print()

    print(filtration_by_state)
    print()

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        print()
        currency_filtering = input().strip().lower()

        if currency_filtering == "да":
            currency_code = "RUB"
            currency_transactions = list(filter_by_currency(filtration_by_state, code=currency_code))
            break
        elif currency_filtering == "нет":
            print("Выводим все транзакции, без учёта валюты.")
            currency_transactions = filtration_by_state
            break
        else:
            print("Неверный выбор валюты. Попробуйте снова I-(")
            print()
            continue  # Возвращаемся к началу цикла

    print(currency_transactions)
    print()

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        print()
        agreement = input().strip().lower()

        if agreement == "да":
            word = input("Введите слово для фильтрации: ").strip()
            # Проверяем, что слово не пустое
            if word:
                filtering_by_word = search_transactions(transactions=transactions, search_term=word)
                print(f"Отфильтрованные транзакции по слову '{word}':")
                print(filtering_by_word)  # Выводим отфильтрованные транзакции
                break
            break
        elif agreement == "нет":
            print("Будет выведены транзакции без фильтрации по слову в описании.")
            print()
            filtering_by_word = currency_transactions
            break
        else:
            print("Повторите запрос. Непонятно, что вы хотите.")
            print()
            continue

    print()
    print("Распечатываю итоговый список транзакций...")
    print()

    counter = 0

    for fil in filtering_by_word:
        if "id" in fil:
            counter += 1

    print(f"Всего банковских операций в выборке: {counter}")
    print()

    if filtering_by_word:

        for transaction in filtering_by_word:

            short_shelf_life = get_date(date=transaction.get("date"))
            payment_status = transaction.get("description")
            payment_method = mask_account_card(string=transaction.get("to", ""))
            sum_filter = transaction["operationAmount"]["amount"]
            currency_name = transaction["operationAmount"]["currency"]["name"]

            print(f"Дата: {short_shelf_life} {payment_status}, {payment_method}, Сумма: {sum_filter} {currency_name}")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")



if __name__ == "__main__":
    main()


# print(main())


# python main.py
# black main.py
# flake8 main.py
# mypy main.py
# isort main.py
