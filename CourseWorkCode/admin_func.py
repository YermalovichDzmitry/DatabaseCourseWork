import mysql.connector

conn = mysql.connector.connect(host="localhost", port="3306", user="dima", password="12345678",
                               database="school_data_base")


def find_student_id(name_):
    query = "SELECT student_id,name,class_name,diary_id \
        FROM student\
        INNER JOIN class ON class.class_id = student.class_id\
        WHERE name = %s"
    val = (name_,)
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        data = cursor.fetchall()
        for i in range(len(data)):
            print(f"Id = {data[i][0]}")
            print(f"Name = {data[i][1]}")
            print(f"Class = {data[i][2]}")
            print(f"Diary id = {data[i][3]}")
            print()


def find_teacher_id(name_):
    query = "SELECT teacher_id \
        FROM teacher\
        WHERE name = %s"
    val = (name_,)
    with conn.cursor() as cursor:
        cursor.execute(query, val)
        data = cursor.fetchall()
        for i in range(len(data)):
            print(f"Teacher id = {data[i][0]}")


def add_teacher_func(teacher_name):
    with conn.cursor() as cursor:
        cursor.callproc('add_teacher', [teacher_name])
        conn.commit()
        print("Successfully append teacher\n")


def create_diary_func():
    with conn.cursor() as cursor:
        cursor.callproc("create_diary")
        conn.commit()
        print("Successfully create diary\n")


def add_student_func(name, class_id, teacher_id, parent_id, diary_id, behavior):
    with conn.cursor() as cursor:
        cursor.callproc("add_student", (name, class_id, teacher_id, parent_id, diary_id, behavior))
        conn.commit()
        print("Successfully add student\n")


def delete_student_func(student_id):
    with conn.cursor() as cursor:
        cursor.callproc("delete_student", [student_id])
        conn.commit()
        print("Successfully delete student\n")


def add_parent_func(parent_gmail, parent_name):
    with conn.cursor() as cursor:
        cursor.callproc("add_parent", (parent_gmail, parent_name))
        conn.commit()
        print("Successfully add parent\n")


def delete_user(user_id_):
    delete_query = f"DELETE FROM users WHERE users_id = {user_id_}"
    with conn.cursor() as cursor:
        cursor.execute(delete_query)
        conn.commit()
        print("Successfully delete user\n")


def add_user_func(login, password, role_id, your_personal_data_id):
    with conn.cursor() as cursor:
        cursor.callproc("add_user", (login, password, role_id, your_personal_data_id))
        conn.commit()
        print("Successfully add user\n")
