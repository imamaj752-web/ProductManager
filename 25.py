from peewee import *

db = SqliteDatabase('system.db')

class Task(Model):
    title = CharField()
    priority = CharField()
    category = CharField()
    class Meta:
        database = db

class Logs(Model):
    user = CharField()
    action = CharField()
    task = ForeignKeyField(Task, backref='logs')
    timestamp = DateTimeField()
    status = CharField()
    class Meta:
        database = db

db.connect()
db.drop_tables([Task, Logs])
db.create_tables([Task, Logs])

tasks_data = [
    (1, "Fix auth bug", "High", "Backend"),
    (2, "Update UI", "Medium", "Frontend"),
    (3, "Database cleanup", "High", "Database"),
    (4, "Refactor code", "Low", "Backend"),
    (5, "Security patch", "High", "Security")
]
Task.insert_many(tasks_data, fields=[Task.id, Task.title, Task.priority, Task.category]).execute()

logs_data = [
    ("admin", "DELETE", 3, "2024-05-01 10:00", "OK"),
    ("ivan", "UPDATE", 2, "2024-05-01 10:05", "FAIL"),
    ("anna", "DELETE", 1, "2024-05-01 10:07", "OK"),
    ("ivan", "DELETE", 3, "2024-05-01 10:10", "OK"),
    ("admin", "UPDATE", 4, "2024-05-01 10:12", "OK"),
    ("anna", "UPDATE", 2, "2024-05-01 10:15", "OK"),
    ("ivan", "DELETE", 5, "2024-05-01 10:20", "OK")
]
Logs.insert_many(logs_data, fields=[Logs.user, Logs.action, Logs.task, Logs.timestamp, Logs.status]).execute()

print("кто чаще всего удалял задачи с высоким приорететом")
q1 = (Logs.select(Logs.user, fn.COUNT(Logs.id).alias('cnt'))
      .join(Task).where((Logs.action == 'DELETE') & (Task.priority == 'High'))
      .group_by(Logs.user).order_by(SQL('cnt').desc()))
for r in q1: print(f"пользователь {r.user}, количество {r.cnt}")

print("\nкакие задачи удаляли больше одного разу")
q2 = (Task.select(Task.title).join(Logs).where(Logs.action == 'DELETE')
      .group_by(Task.title).having(fn.COUNT(Logs.id) > 1))
for r in q2: print(f"Задача: {r.title}")

print("\nКакой пользователь имеет больше все ошибок с работой бекент задач")
r3 = (Logs.select(Logs.user).join(Task)
      .where((Logs.status == 'FAIL') & (Task.category == 'Backend'))
      .group_by(Logs.user).order_by(fn.COUNT(Logs.id).desc()).first())
if r3: print(f"пользователь {r3.user}")

print("\nкакую задачу крайний раз редактировали и кто это сделал")
r4 = (Logs.select(Logs.user, Task.title).join(Task)
      .where(Logs.action == 'UPDATE').order_by(Logs.timestamp.desc()).first())
if r4: print(f"пользователь {r4.user}, задача {r4.task.title}")

print("\nсколько людей работало над задачей секюрити")
r5 = Logs.select(fn.COUNT(Logs.user.distinct())).join(Task).where(Task.category == 'security').scalar()
print(f"количество {r5}")