import csv
from typing import Dict
from typing import List

import pandas as pd

file_transactions_csv = "./data/transactions.csv"


def transactions_csv(file_transactions_csv: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV и выдачи списка словарей с транзакциями"""

    transactions_list_csv = []  # Список для хранения транзакций

    with open(file_transactions_csv, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")  # Указываем разделитель
        # Печать заголовков для отладки
        print("Заголовки CSV:", reader.fieldnames)
        for row in reader:
            # Указываем ключи
            transaction = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "amount": row["amount"],
                "currency_name": row["currency_name"],
                "currency_code": row["currency_code"],
                "from": row["from"],
                "to": row["to"],
                "description": row["description"],
            }
            transactions_list_csv.append(transaction)  # Добавляем транзакцию в список

    return transactions_list_csv  # Возвращаем список транзакций


# print(transactions_csv(file_transactions_csv))


file_transactions_excel_xlsx = "./data/transactions_excel.xlsx"


def transactions_excel_xlsx(file_transactions_excel_xlsx: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel и выдачи списка словарей с транзакциями."""

    transactions_list_excel_xlsx = []  # Список для хранения транзакций

    excel_data = pd.read_excel(file_transactions_excel_xlsx)  # Чтение Excel-файла

    for index, row in excel_data.iterrows():
        # Указываем ключи
        transaction: Dict[str, str] = {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "amount": row["amount"],
            "currency_name": row["currency_name"],
            "currency_code": row["currency_code"],
            "from": row["from"],
            "to": row["to"],
            "description": row["description"],
        }
        transactions_list_excel_xlsx.append(transaction)  # Добавляем транзакцию в список

    return transactions_list_excel_xlsx  # Возвращаем список транзакций


# print(transactions_excel_xlsx(file_transactions_excel_xlsx))


# python src/finance.py
# black src/finance.py
# flake8 src/finance.py
# mypy src/finance.py
# isort src/finance.py
