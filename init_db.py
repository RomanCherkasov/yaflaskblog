import sqlite3 # библиотека для работы с sqlite3
# открываем соединение с файлом базы данных
# если его нет, не переживаем, он будет создан автоматически
connection = sqlite3.connect('database.db') 

# выполняем наш скрипт для создание таблицы post который мы написали ранее
with open('schema.sql') as f:
    connection.executescript(f.read())

# создаем курсор для использования метода "execute"
cur = connection.cursor()
# добавляем записи в таблицу post. Заполняем только title и content
# остальные поля заполнятся автоматически силами базы данных
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", # долго ловил ошибку в названии не post a posts
             ('Первый пост!!!', 'Привет студентам ЯПрактикума!!!')
             )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
             ('Второй пост!!!', 'Привет студентам ЯПрактикума ещё раз!!!')
             )

# commit - выполняет все действия что были сделаны выше(?)
connection.commit()
# обязательно закрываем соединение
connection.close()