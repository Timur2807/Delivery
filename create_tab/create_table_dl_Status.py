"""
В этом модуле представлены методы создания таблицы в БД, и заполнения таблицы.

Страница Delivery_Status_Current
"""

import sqlite3
import openpyxl

DB_NAME = '../db.sqlite3'




def create_table_two():
    """Метод создания таблицы с 2 страницы."""
    with sqlite3.connect(DB_NAME) as sqlite_conn:
        sql_request = """CREATE TABLE IF NOT EXISTS Delivery_Status_Current (
            InternalId integer PRIMARY KEY,
            StatusName varchar(50) NOT NULL,
            LoadDate date NOT NULL
            );"""
        sqlite_conn.execute(sql_request)


def into_sheet_two():
    """Метод заполнения БД с второй страницы."""
    book = openpyxl.reader.excel.load_workbook(filename='DeliveryData.xlsx', data_only=True)
    book.active = 1
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
        sql_request = "INSERT INTO Delivery_Status_Current VALUES (?,?,?)"
        for value in values:
            sqlite_conn.execute(sql_request, value)
        sqlite_conn.commit()


# create_table_two()
# into_sheet_two()
