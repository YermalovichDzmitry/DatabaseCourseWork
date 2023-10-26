import mysql.connector

conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="root", database="bsuir_bd")


def get_all_from_users():
    query = "SELECT * FROM users"
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()


def get_all_from_student():
    query = "SELECT * FROM student"
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()


def get_all_from_parent():
    query = "SELECT * FROM parent"
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()


def get_all_from_teacher():
    query = "SELECT * FROM teacher"
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()
