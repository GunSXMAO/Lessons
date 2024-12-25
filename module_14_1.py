import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

# Заполнение таблицы 10 записями
for i in range(1, 11):
    username = f'User{i}'
    email = f'example{i}@example.com'
    age = i * 10
    balance = 1000
    cursor.execute('INSERT INTO users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, balance))
connection.commit()

# Обновление balance у каждой второй записи
for i in range(1, 11, 2):
    cursor.execute('UPDATE users SET balance = 500 WHERE id = ?', (i,))
connection.commit()

# Удаление каждой третьей записи
for i in range(1, 11, 3):
    cursor.execute('DELETE FROM users WHERE id =?', (i,))
connection.commit()

# Выборка всех записей, где возраст не равен 60, и вывод
cursor.execute("SELECT username, email, age, balance FROM users WHERE age != 60")
rows = cursor.fetchall()
for row in rows:
    username, email, age, balance = row
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")
