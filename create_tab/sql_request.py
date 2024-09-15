"""
Здесь представлены методы по запросу данных из таблиц.
Возможно они упадут ввиду того что возникли проблемы с импортом таблиц в БД.
"""



import sqlite3

DB_NAME = '../db.sqlite3'


def status_done():
    """
    Метод запрашивает
    Количество успешно завершенных заказов
    и их среднее время выполнения в разрезе городов.
    """
    with sqlite3.connect(DB_NAME) as sqlit_conn:
        sql_request = """SELECT COUNT(*) 
            FROM Delivery_Status_Current 
            WHERE StatusName='Done' 
            UNION 
            SELECT AVG(DeliveryTime)
            FROM Delivery_Requests
            GROUP BY DeliveryCity
            """
        sql_cursor = sqlit_conn.execute(sql_request)
        # for record in sql_cursor:
        #     print(record)
        records = sql_cursor.fetchall()
        print(records)


def count():
    """
    Метод запрашивает
    Количество заявок в разрезе статусов,
    которые поступили за последние 3 недели
    с типом доставки «Письмо» и «Бандероль».
    """
    with sqlite3.connect(DB_NAME) as sqlit_conn:
        sql_request = """SELECT COUNT(*) 
        FROM Delivery_Requests 
        WHERE LoadDate BETWEEN '2024-08-18' AND '2024-09-08'
        HAVING PackageType IN ('Letter', 'Parcel')
        UNION 
        SELECT COUNT(*)
        FROM Delivery_Status_Current
        WHERE LoadDate BETWEEN '2024-08-18' AND '2024-09-08'
        GROUP BY StatusName
        """
        sql_cursor = sqlit_conn.execute(sql_request)
        records = sql_cursor.fetchall()
        print(records)


def avg_time():
    """
    Среднее время нахождение заявки на каждом этапе в городе Казань
    в разрезе типа посылки для завершенных заявок. """
    with sqlite3.connect(DB_NAME) as sqlit_conn:
        sql_request = """SELECT AVG(DeliveryTime) 
        FROM Delivery_Requests
        WHERE DeliveryCity='Казань'
        INNER JOIN Delivery_Status_History
        GROUP BY StatusName='Done'
        """
        sql_cursor = sqlit_conn.execute(sql_request)
        records = sql_cursor.fetchall()
        print(records)

