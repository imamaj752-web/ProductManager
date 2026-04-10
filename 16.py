import sqlite3

connection = sqlite3.connect('house.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT
      )
""")
connection.close()