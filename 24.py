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

print("1. Студенты, записанные более чем на 1 курс:")
query = (Student
         .select(Student, fn.COUNT(Enrollment.course).alias('course_count'))
         .join(Enrollment)
         .group_by(Student)
         .having(fn.COUNT(Enrollment.course) > 1))
for student in query:
    print(f"  {student.name} - {student.course_count} курса")

print("\n2. Студенты из Киева, посещающие курсы:")
query = (Student
         .select()
         .join(Enrollment)
         .where(Student.city == "Київ")
         .distinct())
for student in query:
    print(f"  {student.name}")

print("\n3. Студенты преподавателя Ирина:")
query = (Student
         .select()
         .join(Enrollment)
         .join(Course)
         .where(Course.teacher == "Ірина")
         .distinct())
for student in query:
    print(f"  {student.name}")

print("\n4. Количество студентов у каждого преподавателя:")
query = (Course
         .select(Course.teacher, fn.COUNT(Enrollment.student).alias('student_count'))
         .join(Enrollment, JOIN.LEFT_OUTER)
         .group_by(Course.teacher))
for course in query:
    print(f"  {course.teacher}: {course.student_count}")

print("\n5. Преподаватели без студентов:")
query = (Course
         .select(Course.teacher)
         .join(Enrollment, JOIN.LEFT_OUTER)
         .group_by(Course.teacher)
         .having(fn.COUNT(Enrollment.id) == 0))
for course in query:
    print(f"  {course.teacher}")

db.close()