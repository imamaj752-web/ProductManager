import peewee
from playhouse.shortcuts import model_to_dict
db = peewee.SqliteDatabase('memory')
class Student(peewee.Model):
    name = peewee.CharField()
    age = peewee.IntegerField()
    grade = peewee.IntegerField()
    city = peewee.CharField()
    class Meta:
        database = db
db.connect()
db.create_tables([Student])
data = [
    ('Анна', 12, 95, 'Київ'),
    ('Олег', 13, 82, 'Львів'),
    ('Марта', 12, 74, 'Одеса'),
    ('Дмитро', 14, 89, 'Київ'),
    ('Ірина', 13, 95, 'Харків'),
    ('Софія', 12, 78, 'Львів'),
]
Student.insert_many(data, fields=[Student.name, Student.age, Student.grade, Student.city]).execute()
print("1.1 между 80 и 90:")
for s in Student.select().where(Student.grade.between(80, 90)):
    print(s.name, s.grade)
print("\n1.2 имена и места кому 12")
for s in Student.select().where(Student.age == 12):
    print(s.name, s.city)
print("\n1.3 не с киева:")
for s in Student.select().where(Student.city != 'Київ'):
    print(s.name, s.city)
print("\n1.4 уникальние места:")
for city in Student.select(Student.city).distinct():
    print(city.city)
print("\n2.1 за возрастом спадання")
for s in Student.select().order_by(Student.age.desc()):
    print(s.name, s.age)
print("\n2.2 за местом потом оценкой:")
for s in Student.select().order_by(Student.city, Student.grade):
    print(s.city, s.name, s.grade)
print("\n3.3 самая большая оценка:")
for s in Student.select().order_by(Student.grade.desc()).limit(3):
    print(s.name, s.grade)
print("\n4. с полем performance:")
for s in Student.select():
    if s.grade >= 90:
        perf = 'афигенно'
    elif s.grade >= 80:
        perf = 'хорошо'
    else:
        perf = 'потдягиваться надо'
    print(s.name, s.grade, perf)
print("\n5.1 с каждого места:")
for city in Student.select(Student.city, peewee.fn.COUNT(Student.id).alias('count')).group_by(Student.city):
    print(city.city, city.count)
print("\n5.2 сер.возраст")
avg_age = Student.select(peewee.fn.AVG(Student.age).alias('avg')).scalar()
print(f"{avg_age:.2f}")
print("\n5.3 макс возраст с львова")
max_age = Student.select(peewee.fn.MAX(Student.age)).where(Student.city == 'Львів').scalar()
print(max_age)
print("\n6. Сер. бал > 85 по местам:")
for city in (Student
        .select(Student.city, peewee.fn.AVG(Student.grade).alias('avg_grade'))
        .group_by(Student.city)
        .having(peewee.fn.AVG(Student.grade) > 85)):
    print(city.city, f"{city.avg_grade:.2f}")

db.close()