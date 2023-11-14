import mysql.connector

conn = mysql.connector.connect(host="localhost", port="3306", user="dima", password="12345678",
                               database="school_data_base")


def rate_english(id_, mark):
    query = "UPDATE diary SET english_score = CONCAT(english_score,' ',%s) WHERE diary.diary_id = %s"
    val = (mark, id_)
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        conn.commit()
        print("Success update")


def rate_math(id_, mark):
    query = "UPDATE diary SET math_score = CONCAT(math_score,' ',%s) WHERE diary.diary_id = %s"
    val = (mark, id_)
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        conn.commit()
        print("Success update")


def find_teacher_classes(id_):
    query = "SELECT name,class_name\
              FROM class_teacher\
              INNER JOIN class ON class.class_id = class_teacher.class_id\
              INNER JOIN teacher ON teacher.teacher_id = class_teacher.teacher_id\
              WHERE teacher.teacher_id=%s"
    val = (id_,)
    cl = []
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        data = cursor.fetchall()
        for d in data:
            print(f"Teacher class is {d[1]}")
            cl.append(d[1])
    return cl


def find_student_from_class(class_name_):
    query = "SELECT student_id,name,class_name,diary_id \
        FROM student\
        INNER JOIN class ON class.class_id = student.class_id\
        WHERE class_name = %s"
    val = (class_name_,)
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        data = cursor.fetchall()
        for i in range(len(data)):
            print(f"Id = {data[i][0]}")
            print(f"Name = {data[i][1]}")
            print(f"Class = {data[i][2]}")
            print(f"Diary id = {data[i][3]}")
            print()
