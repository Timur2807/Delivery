"""
В этом модуле представлены методы создания таблицы в БД, и заполнения таблицы.

Страница Delivery_Status_History
"""

import sqlite3
import openpyxl

DB_NAME = '../db.sqlite3'



def create_table_three():
    """Метод создания таблицы с 3 страницы. """
    with sqlite3.connect(DB_NAME) as sqlite_conn:
        sql_request = """CREATE TABLE IF NOT EXISTS Delivery_Status_History (
            InternalId integer PRIMARY KEY,
            StatusName varchar(50) NOT NULL,
            LoadDate date NOT NULL
            );"""
        sqlite_conn.execute(sql_request)


def into_sheet_three():
    """Метод заполнения БД с 3 страницы."""
    book = openpyxl.reader.excel.load_workbook(filename='DeliveryData.xlsx', data_only=True)
    book.active = 2
    sheet = book.active

    values = []

    for row in range(2, sheet.max_row + 1):
        values.append(
            (sheet['A' + str(row)].value,
             sheet['B' + str(row)].value,
             sheet['C' + str(row)].value,
             )
        )

    with sqlite3.connect(DB_NAME) as sqlite_conn:
        sql_request = "INSERT or IGNORE INTO Delivery_Status_History VALUES (?,?,?)"
        for value in values:
            sqlite_conn.execute(sql_request, value)
        sqlite_conn.commit()


# create_table_three()
# into_sheet_three()
