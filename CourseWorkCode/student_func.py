import mysql.connector

conn = mysql.connector.connect(host="localhost", port="3306", user="dima", password="12345678",
                               database="school_data_base")


def add_complain(reason_, student_id_, teacher_id_):
    query = "INSERT INTO complaints(reason,student_id,teacher_id) VALUES (%s,%s,%s)"
    val = (reason_, student_id_, teacher_id_)
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        conn.commit()
        print("Insert success")


def get_english_score(diary_id_):
    query = "SELECT english_score FROM diary WHERE diary_id = %s"
    val = (diary_id_,)
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        data = cursor.fetchall()

        print(f"Your english mark: {data[0][0]}")


def get_math_score(diary_id_):
    query = "SELECT math_score FROM diary WHERE diary_id = %s"
    val = (diary_id_,)
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        data = cursor.fetchall()

        print(f"Your english mark: {data[0][0]}")
