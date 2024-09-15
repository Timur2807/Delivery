"""
В этом модуле представлены методы создания таблицы в БД, и заполнения таблицы.

Страница Delivery_Requests

"""

import sqlite3
import openpyxl
import datetime

DB_NAME = '../db.sqlite3'


def create_table_one(file):
    """Метод создания Таблицы 1 листа"""
    with sqlite3.connect(file) as sqlite_conn:
        sql_request = """CREATE TABLE IF NOT EXISTS Delivery_Requests (
            InternalId integer PRIMARY KEY,
            LoadDate date NOT NULL,
            CustomerName varchar(50) NOT NULL,
            DeliveryCity varchar(50) NOT NULL,
            DeliveryAddress varchar(200) NOT NULL,
            DeliveryDate date NOT NULL,
            DeliveryTime time NOT NULL,
            PackageType varchar(50) NOT NULL,
            Comment varchar(100));"""
        sqlite_conn.execute(sql_request)


def into_sheet_one():
    """Метод заполнения БД с первой страницы."""
    book = openpyxl.reader.excel.load_workbook(filename='DeliveryData.xlsx', data_only=True)
    book.active = 0
    sheet = book.active

    values = []

    for row in range(2, sheet.max_row + 1):
        values.append(
            (sheet['A' + str(row)].value,
             sheet['B' + str(row)].value,
             sheet['C' + str(row)].value,
             sheet['D' + str(row)].value,
             sheet['E' + str(row)].value,
             sheet['F' + str(row)].value,
             sheet['G' + str(row)].value,
             sheet['H' + str(row)].value,
             sheet['I' + str(row)].value,

             )
        )

    with sqlite3.connect(DB_NAME) as sqlite_conn:
        sql_request = "INSERT or IGNORE INTO Delivery_Requests VALUES (?,?,?,?,?,?,?,?,?)"
        for value in values:
            sqlite_conn.execute(sql_request, value)
        sqlite_conn.commit()

# create_table_one(DB_NAME)
# into_sheet_one()
