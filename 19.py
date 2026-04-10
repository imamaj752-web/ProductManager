import sqlite3

conn = sqlite3.connect('games.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT,
    rating REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS game_stats (
    game_id INTEGER,
    active_players INTEGER,
    avg_playtime INTEGER,
    FOREIGN KEY (game_id) REFERENCES games(id)
)
''')

cursor.execute("DELETE FROM games")
cursor.execute("DELETE FROM game_stats")

games_data = [
    ('Minecraft', 'Sandbox', 9.1),
    ('Fortnite', 'Shooter', 8.5),
    ('The Sims 4', 'Simulation', 8.0),
    ('FIFA 23', 'Sports', 7.8),
    ('Among Us', 'Party', 8.3),
    ('Cyberpunk 2077', 'RPG', 7.4),
    ('Mario Kart', 'Racing', 8.6)
]

cursor.executemany('INSERT INTO games (title, genre, rating) VALUES (?, ?, ?)', games_data)

stats_data = [
    (1, 50000000, 120),
    (2, 42000000, 90),
    (3, 26000000, 70),
    (4, 25000000, 80),
    (5, 31000000, 45),
    (6, 15000000, 100),
    (7, 27000000, 60)
]

cursor.executemany('INSERT INTO game_stats (game_id, active_players, avg_playtime) VALUES (?, ?, ?)', stats_data)

conn.commit()

print("1. выборк")
print()
cursor.execute('SELECT title, genre FROM games WHERE rating > 8.0')
print("Игры с рейтингом выше 8.0:")
for row in cursor.fetchall():
    print(f"  {row[0]} ({row[1]})")

print()
cursor.execute('SELECT title, genre, rating FROM games ORDER BY rating DESC')
print("игры отсортированные по рейтингу (убывание):")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} - {row[2]}")

russian_genres = {
    'Sandbox': 'песочница',
    'Shooter': 'шутер',
    'Simulation': 'симулятор',
    'Sports': 'спорт',
    'Party': 'вечеринка',
    'RPG': 'рпн',
    'Racing': 'гонки'
}

print()
cursor.execute('SELECT title, genre FROM games')
print("игры с рус жанрами:")
for row in cursor.fetchall():
    ru_genre = russian_genres.get(row[1], row[1])
    print(f"  {row[0]}: {ru_genre}")

print()
cursor.execute('''
SELECT g.title, s.avg_playtime 
FROM games g 
JOIN game_stats s ON g.id = s.game_id 
WHERE s.avg_playtime > 80
''')
print("Игры со средним временем игры более 80 минут:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} мин")

print()
print("2. функии")
print()
cursor.execute('SELECT AVG(rating) FROM games')
avg_rating = cursor.fetchone()[0]
print(f"средний рейтинг всех игр: {avg_rating:.2f}")

print()
cursor.execute('SELECT SUM(active_players) FROM game_stats')
total_players = cursor.fetchone()[0]
print(f"общее количество активных игроков: {total_players:,}")

print()
cursor.execute('''
SELECT g.title, s.avg_playtime 
FROM games g 
JOIN game_stats s ON g.id = s.game_id 
ORDER BY s.avg_playtime DESC 
LIMIT 1
''')
max_playtime = cursor.fetchone()
if max_playtime:
    print(f"игра с наибольшим средним временем игры: {max_playtime[0]} ({max_playtime[1]} мин)")

print()
cursor.execute('SELECT MIN(rating) FROM games')
min_rating = cursor.fetchone()[0]
print(f"минимальный рейтинг среди игр: {min_rating}")

print()
print("3. ограничение")
print()
cursor.execute('''
SELECT g.title, s.active_players 
FROM games g 
JOIN game_stats s ON g.id = s.game_id 
ORDER BY s.active_players DESC 
LIMIT 3
''')
print("три самые популярные игры по количеству активных игроков:")
for i, row in enumerate(cursor.fetchall(), 1):
    print(f"  {i}. {row[0]}: {row[1]:,} игроков")

print()
print("4. групировка и сортировк")
print()
cursor.execute('''
SELECT genre, AVG(rating) as avg_rating
FROM games
GROUP BY genre
ORDER BY avg_rating DESC
''')
print("Средний рейтинг по жанрам:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]:.2f}")

print()
cursor.execute('''
SELECT g.genre, SUM(s.active_players) as total_players
FROM games g
JOIN game_stats s ON g.id = s.game_id
GROUP BY g.genre
ORDER BY total_players DESC
''')
print("общее количество игроков в каждом жанр:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]:,} игроков")

print()
print("5. условие")
print()
cursor.execute('''
SELECT 
    g.title, 
    s.active_players,
    CASE 
        WHEN s.active_players > 40000000 THEN 'Хит'
        WHEN s.active_players BETWEEN 20000000 AND 40000000 THEN 'популярние'
        ELSE 'обычная'
    END as popularity_level
FROM games g
JOIN game_stats s ON g.id = s.game_id
ORDER BY s.active_players DESC
''')
print("уровень популярност игр:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]:,} игроков - {row[2]}")

conn.close()

print()
print("все сделано")