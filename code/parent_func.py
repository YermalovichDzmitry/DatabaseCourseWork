import mysql.connector

conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="root", database="bsuir_bd")


def add_meeting(reason_, parent_id_, teacher_id_):
    query = "INSERT INTO school_meetings(reason,parent_id,teacher_id) VALUES (%s,%s,%s)"
    val = (reason_, parent_id_, teacher_id_)
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        conn.commit()
        print("Insert success")
