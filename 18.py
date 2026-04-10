from peewee import *
db = SqliteDatabase('test.db')
db.connect()
class Student(Model):
    id = AutoField(primary_key=True)  # можна не створювати
    name = CharField()
    age = IntegerField()
    grade = FloatField()
    city = CharField()
    class Meta:
        database = db
        table_name = 'student'
db.create_tables([Student])
db.close()