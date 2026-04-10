from peewee import *

db = SqliteDatabase('school.db')
db.connect()

class Student(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    age = IntegerField()
    city = CharField()

    class Meta:
        database = db
        table_name = 'student'


class Course(Model):
    id = AutoField(primary_key=True)
    title = CharField()
    teacher = CharField()

    class Meta:
        database = db
        table_name = 'course'


class Enrollment(Model):
    id = AutoField(primary_key=True)

    # enrollments - список курсів, на які записаний студент
    student = ForeignKeyField(Student, backref="enrollments")

    # students - список студентів, які записані на цей курс
    course = ForeignKeyField(Course, backref="students")

    class Meta:
        database = db
        table_name = 'enrollment'


# db.drop_tables([Student, Course, Enrollment])
# db.create_tables([Student, Course, Enrollment])
#
# students = [
#     {"name": "Анна", "age": 12, "city": "Київ"},
#     {"name": "Олег", "age": 13, "city": "Львів"},
#     {"name": "Ірина", "age": 14, "city": "Одеса"},
#     {"name": "Марта", "age": 13, "city": "Київ"},
#     {"name": "Тарас", "age": 15, "city": "Харків"},
#     {"name": "Олена", "age": 14, "city": "Луцьк"},
#     {"name": "Влад", "age": 12, "city": "Київ"},
#     {"name": "Катя", "age": 13, "city": "Чернівці"},
#     {"name": "Максим", "age": 14, "city": "Львів"},
#     {"name": "Поліна", "age": 12, "city": "Суми"},
# ]
# courses = [
#     {"title": "Python", "teacher": "Ірина"},
#     {"title": "Mathematics", "teacher": "Олег"},
#     {"title": "Roblox Studio", "teacher": "Анна"},
#     {"title": "Web Development", "teacher": "Анна"},
#     {"title": "Physics", "teacher": "Олег"},
#     {"title": "English", "teacher": "Марина"},
#     {"title": "3D Modeling", "teacher": "Давид"},
# ]
# enrollments = [
#     {"student": 1, "course": 1},
#     {"student": 1, "course": 4},
#     {"student": 2, "course": 2},
#     {"student": 3, "course": 1},
#     {"student": 4, "course": 3},
#     {"student": 5, "course": 3},
#     {"student": 6, "course": 5},
#     {"student": 7, "course": 1},
#     {"student": 8, "course": 4}
# ]
#
# Student.insert_many(students).execute()
# Course.insert_many(courses).execute()
# Enrollment.insert_many(enrollments).execute()


'''Показати всіх студентів і курси, на які вони записані'''

query = (
    Enrollment
    .select(Student.name, Course.title)
    .join(Student)
    .switch(Enrollment)  # повертаємось до потрібної таблиці
    .join(Course)
)

for row in query:
    print(f'{row.student.name} -> {row.course.title}')


'''Показати тільки тих, хто навчається на “Python”'''
query = (
    Enrollment
    .select(Student.name, Course.title)
    .join(Student)
    .switch(Enrollment)
    .join(Course)
    .where(Course.title == "Python")

)

for record in query:
    print(f"{record.student.name} -> {record.course.title}")

'''Усі студенти, навіть без курсу'''

query = (
    Student
    .select(Student, Course)
    .join(Enrollment, JOIN.LEFT_OUTER)
    .join(Course, JOIN.LEFT_OUTER)
)

for student in query:
    if student.enrollments:
        print(student.name)
        for enrollment in student.enrollments:
            print(enrollment.course.title)
        print('\n')
    else:
        print(f'{student.name} немає курсів')


'''Показати студентів, які не відвідують жодного курсу (тільки таких)'''

query = (
    Student
    .select(Student.name)
    .join(Enrollment, JOIN.LEFT_OUTER)
    .where(Enrollment.id.is_null())
)

for student in query:
    print(student.name)


'''Показати найпопулярніший курс (той, що має найбільшу кількість студентів)'''

query = (
    Course
    .select(Course.title, fn.COUNT(Enrollment.student).alias('amount_students'))
    .join(Enrollment)
    .group_by(Course.title)

    .order_by(fn.COUNT(Enrollment.student).desc())
    .limit(1)
)

for course in query:
    print(f'{course.title}: {course.amount_students}')


'''Знайти викладача, який веде найбільше курсів'''

query = (
    Course
    .select(Course.teacher, fn.COUNT(Course.title).alias('amount_courses'))
    .group_by(Course.teacher)

    .order_by(fn.COUNT(Course.title).desc())
    .limit(2)
)

for record in query:
    print(f"{record.teacher}: {record.amount_courses}")
    from peewee import *

    db = SqliteDatabase('school.db')


    class Student(Model):
        id = AutoField(primary_key=True)
        name = CharField()
        age = IntegerField()
        city = CharField()

        class Meta: database = db; table_name = 'student'


    class Course(Model):
        id = AutoField(primary_key=True)
        title = CharField()
        teacher = CharField()

        class Meta: database = db; table_name = 'course'


    class Enrollment(Model):
        id = AutoField(primary_key=True)
        student = ForeignKeyField(Student, backref="enrollments")
        course = ForeignKeyField(Course, backref="students")

        class Meta: database = db; table_name = 'enrollment'


    db.connect()

    print("1. Студенты записани больше чем на 1 курс")
    query = (Student.select(Student, fn.COUNT(Enrollment.course).alias('cnt'))
             .join(Enrollment).group_by(Student).having(fn.COUNT(Enrollment.course) > 1))
    for s in query: print(f"{s.name}: {s.cnt} курса")

    print("\n2. Студенти из киева которые посещают курси")
    query = (Student.select().join(Enrollment).where(Student.city == "Киев").distinct())
    for s in query: print(s.name)

    print("\n3. Студенты преподовател Ирина:")
    query = (Student.select().join(Enrollment).join(Course).where(Course.teacher == "Ірина").distinct())
    for s in query: print(s.name)

    print("\n4. сколько студентов у кажлого учителя")
    query = (Course.select(Course.teacher, fn.COUNT(Enrollment.student).alias('total'))
             .join(Enrollment, JOIN.LEFT_OUTER).group_by(Course.teacher))
    for c in query: print(f"{c.teacher}: {c.total}")

    print("\n5. Учитель без студентов")
    query = (Course.select(Course.teacher).join(Enrollment, JOIN.LEFT_OUTER)
             .group_by(Course.teacher).having(fn.COUNT(Enrollment.id) == 0))
    for c in query: print(c.teacher)
