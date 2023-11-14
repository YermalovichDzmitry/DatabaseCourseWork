import mysql.connector
import admin_func
import common_func
import student_func
import teacher_func
import parent_func
import re

conn = mysql.connector.connect(host="localhost", port="3306", user="dima", password="12345678",
                               database="school_data_base")

allowed_key = False
try:

    print("Hello! This is school application")
    while True:
        print(f"Enter your email please:")
        email = input()
        print(f"Enter your password please:")
        password = input()
        role_ = None
        password_ = None
        your_personal_data = None
        with conn.cursor() as cursor:
            data = cursor.callproc('get_user_data', (email, role_, password_, your_personal_data))
            if data[1] is None:
                print("Your login isn't in database.\nDo you wan't to try enter again\nYes/No ")
                flag_1 = input()
                if flag_1 == "Yes":
                    continue
                else:
                    break

            else:
                if data[2] == password:
                    print("Access is allowed")
                    allowed_key = True
                    break
                else:
                    print("Password error.\nDo you wan't to try enter again\nYes/No")
                    flag_1 = input()
                    if flag_1 == "Yes":
                        continue
                    else:
                        break
finally:
    pass
role_ = data[1]

s = data[0]
result = re.search("[A-Z|a-z]+", s)
name = result.group(0)

if allowed_key:
    if role_ == 1:
        print(f"Hello admin")
        while True:
            print("Select action")
            print(
                "1) Add new teacher\n2) Create new diary\n3) Add student\n4) Delete student\n5) Add parent\n6) Delete user\n7) Get all from user\n8) Get all from teacher\n9) Get all from student\n10) Get all from parent\n11) Find info about student by name\n12) Find teacher id\n13) Add administrator id\n14) Exit")
            choice = int(input())
            try:
                if choice == 1:
                    try:
                        print("Enter teacher name:")
                        teacher_name = input()
                        admin_func.add_teacher_func(teacher_name)
                    except:
                        print("Error")
                elif choice == 2:
                    admin_func.create_diary_func()
                elif choice == 3:
                    print("Enter student name:")
                    student_name = input()
                    print("Enter class id:")
                    class_id = input()
                    print("Enter teacher id:")
                    teacher_id = input()
                    print("Enter parent id:")
                    parent_id = input()
                    print("Enter diary id:")
                    diary_id = input()
                    print("Enter behavior:")
                    behavior = input()
                    admin_func.add_student_func(student_name, class_id, teacher_id, parent_id, diary_id, behavior)
                elif choice == 4:
                    print("Enter student id:")
                    student_id = int(input())
                    admin_func.delete_student_func(student_id)
                elif choice == 5:
                    print("Enter parent_name:")
                    parent_name = input()
                    print("Enter parent_gmail:")
                    parent_gmail = input()
                    admin_func.add_parent_func(parent_gmail, parent_name)
                # elif choice == 6:
                #     print("Enter login:")
                #     login = input()
                #     print("Enter password:")
                #     password = input()
                #     print("Enter role_id:")
                #     role_id = input()
                #     print("Enter your_personal_data_id:")
                #     your_personal_data_id = input()
                #     admin_func.add_user_func(login, password, role_id, your_personal_data_id)
                elif choice == 6:
                    print("Enter user_id:")
                    user_id = input()
                    admin_func.delete_user(user_id)
                elif choice == 7:
                    common_func.get_all_from_users()
                elif choice == 8:
                    common_func.get_all_from_teacher()
                elif choice == 9:
                    common_func.get_all_from_student()
                elif choice == 10:
                    common_func.get_all_from_parent()
                elif choice == 11:
                    print("Enter student name:")
                    name_ = input()
                    admin_func.find_student_id(name_)
                elif choice == 12:
                    print("Enter teacher name:")
                    name_ = input()
                    admin_func.find_teacher_id(name_)
                elif choice == 13:
                    print("Enter admin name:")
                    name_ = input()
                    query = "INSERT INTO administrator(name) VALUES (%s)"
                    val = (name_,)
                    with conn.cursor() as cursor:
                        cursor.execute(query, val)
                        conn.commit()
                    print("Success operation")
                elif choice == 14:
                    print("Bye")
                    break
            except:
                print("Error")
    elif role_ == 2:
        print(f"Hello student")

        stud_id = None
        if name:
            query = "SELECT student_id FROM student WHERE name = %s"
            val = (name,)
            with conn.cursor() as cursor:
                cursor.execute(query, val)
                data = cursor.fetchall()
                if len(data) == 1:
                    stud_id = data[0][0]
                elif len(data) > 1:
                    admin_func.find_student_id(name)
                    print("Select your id:")
                    stud_id = int(input())
                else:
                    print("Name not found")

        while True:
            print("Select action")
            print(
                "1) Add complain\n2) Get english marks\n3) Get math marks\n4) Find info about student by name\n5) Find teacher id\n6) Get your english marks\n7) Get your math marks\n8) Exit")
            choice = int(input())
            try:
                if choice == 1:
                    if stud_id:
                        print("Enter reason:")
                        reason_ = input()
                        print("Enter teacher_id_:")
                        teacher_id_ = input()
                        student_func.add_complain(reason_, stud_id, teacher_id_)
                    else:
                        print("We haven't got your student id")
                elif choice == 2:
                    print("Enter your diary_id:")
                    diary_id_ = input()
                    student_func.get_english_score(diary_id_)

                elif choice == 3:
                    print("Enter your diary_id:")
                    diary_id_ = input()
                    student_func.get_math_score(diary_id_)
                elif choice == 4:
                    print("Enter student name:")
                    name_ = input()
                    admin_func.find_student_id(name_)
                elif choice == 5:
                    print("Enter teacher name:")
                    name_ = input()
                    admin_func.find_teacher_id(name_)
                elif choice == 6:
                    if stud_id:
                        query = "SELECT diary_id FROM student WHERE student_id = %s"
                        val = (stud_id,)
                        with conn.cursor() as cursor:
                            cursor.execute(query, val)
                            data = cursor.fetchall()
                        diary_id_ = data[0][0]
                        student_func.get_english_score(diary_id_)
                    else:
                        print("We haven't got your student id")

                elif choice == 7:
                    if stud_id:
                        query = "SELECT diary_id FROM student WHERE student_id = %s"
                        val = (stud_id,)
                        with conn.cursor() as cursor:
                            cursor.execute(query, val)
                            data = cursor.fetchall()
                        diary_id_ = data[0][0]
                        student_func.get_math_score(diary_id_)
                    else:
                        print("We haven't got your student id")
                elif choice == 8:
                    break
            except:
                print("Error")
    elif role_ == 3:
        print(f"Hello teacher")
        teac_id = None
        if name:
            query = "SELECT teacher_id FROM teacher WHERE name = %s"
            val = (name,)
            with conn.cursor() as cursor:
                cursor.execute(query, val)
                data = cursor.fetchall()
                if len(data) == 1:
                    teac_id = data[0][0]
                elif len(data) > 1:
                    admin_func.find_student_id(name)
                    print("Select your id:")
                    teac_id = int(input())
                else:
                    print("Name not found")

        while True:
            print("Select action")
            print(
                "1) Rate english\n2) Rate math\n3) Find info about student by name\n4) Find teacher id\n5) What classes does the teacher teach\n6) Find student from class\n7) Exit")
            choice = int(input())
            try:
                if choice == 1:
                    if teac_id:
                        data = teacher_func.find_teacher_classes(teac_id)
                        teacher_classes = []
                        for cl in data:
                            teacher_classes.append(cl)
                        print("Enter student diary id:")
                        id_ = input()

                        query = "SELECT class_name FROM student INNER JOIN class ON student.class_id = class.class_id WHERE student_id = %s"
                        val = (id_,)
                        with conn.cursor() as cursor:
                            cursor.execute(query, val)
                            data = cursor.fetchall()
                            if data:
                                class_n = data[0][0]
                        print(f"Student class is {class_n}")
                        if class_n in teacher_classes:
                            print("Enter student english mark:")
                            mark = input()
                            teacher_func.rate_english(id_, mark)
                        else:
                            print("This student doesn't study in your class")
                    else:
                        print("We haven't got your teacher id")
                elif choice == 2:
                    if teac_id:
                        data = teacher_func.find_teacher_classes(teac_id)
                        teacher_classes = []
                        for cl in data:
                            teacher_classes.append(cl)
                        print("Enter student diary id:")
                        id_ = input()

                        query = "SELECT class_name FROM student INNER JOIN class ON student.class_id = class.class_id WHERE student_id = %s"
                        val = (id_,)
                        with conn.cursor() as cursor:
                            cursor.execute(query, val)
                            data = cursor.fetchall()
                            if data:
                                class_n = data[0][0]
                        print(f"Student class is {class_n}")
                        if class_n in teacher_classes:
                            print("Enter student math mark:")
                            mark = input()
                            teacher_func.rate_math(id_, mark)
                        else:
                            print("This student doesn't study in your class")
                    else:
                        print("We haven't got your teacher id")
                elif choice == 3:
                    print("Enter student name:")
                    name_ = input()
                    admin_func.find_student_id(name_)
                elif choice == 4:
                    print("Enter teacher name:")
                    name_ = input()
                    admin_func.find_teacher_id(name_)
                elif choice == 4:
                    print("Enter teacher name:")
                    name_ = input()
                    admin_func.find_teacher_id(name_)
                elif choice == 5:
                    print("Enter teacher id:")
                    id_ = input()
                    teacher_func.find_teacher_classes(id_)
                elif choice == 6:
                    print("Enter class name:")
                    class_name_ = input()
                    teacher_func.find_student_from_class(class_name_)
                elif choice == 7:
                    break
            except:
                print("Error")
    elif role_ == 4:
        print(f"Hello parent")

        pare_id = None
        if name:
            query = "SELECT parent_id FROM parent WHERE parent_name = %s"
            val = (name,)
            with conn.cursor() as cursor:
                cursor.execute(query, val)
                data = cursor.fetchall()
                if len(data) == 1:
                    pare_id = data[0][0]
                else:
                    print("Name not found or greater then 1")
        while True:
            print("Select action")
            print(
                "1) Add meeting\n2) Get english marks\n3) Get math marks\n4) Find info about student by name\n5) Find teacher id\n6) Get your child english marks\n7) Get your child math marks\n8) Exit")
            choice = int(input())
            try:
                if choice == 1:
                    if pare_id:
                        print("Enter reason:")
                        reason_ = input()
                        # print("Enter your_id_:")
                        # student_id_ = input()
                        print("Enter teacher_id_:")
                        teacher_id_ = input()
                        parent_func.add_meeting(reason_, pare_id, teacher_id_)
                    else:
                        print("We haven't got your parent id")

                elif choice == 2:
                    print("Enter your diary_id:")
                    diary_id_ = input()
                    student_func.get_english_score(diary_id_)

                elif choice == 3:
                    print("Enter your diary_id:")
                    diary_id_ = input()
                    student_func.get_math_score(diary_id_)
                elif choice == 4:
                    print("Enter student name:")
                    name_ = input()
                    admin_func.find_student_id(name_)
                elif choice == 5:
                    print("Enter teacher name:")
                    name_ = input()
                    admin_func.find_teacher_id(name_)
                elif choice == 6:

                    query = "SELECT diary_id FROM student WHERE parent_id = %s"
                    val = (pare_id,)
                    with conn.cursor() as cursor:
                        cursor.execute(query, val)
                        data = cursor.fetchall()
                    children = []
                    for d in data:
                        children.append(d[0])
                    for ch in children:
                        query = "SELECT name FROM student WHERE diary_id = %s"
                        val = (ch,)
                        with conn.cursor() as cursor:
                            cursor.execute(query, val)
                            data = cursor.fetchall()
                        name = data[0][0]
                        print(f"Child {name}:")
                        student_func.get_english_score(ch)

                elif choice == 7:
                    query = "SELECT diary_id FROM student WHERE parent_id = %s"
                    val = (pare_id,)
                    with conn.cursor() as cursor:
                        cursor.execute(query, val)
                        data = cursor.fetchall()
                    children = []
                    for d in data:
                        children.append(d[0])
                    for ch in children:
                        query = "SELECT name FROM student WHERE diary_id = %s"
                        val = (ch,)
                        with conn.cursor() as cursor:
                            cursor.execute(query, val)
                            data = cursor.fetchall()
                        name = data[0][0]
                        print(f"Child {name}:")
                        student_func.get_math_score(ch)
            except:
                print("Error")

    else:
        print(f"How are you?")

conn.close()
