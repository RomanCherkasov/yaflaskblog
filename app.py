import sqlite3
from sqlite3.dbapi2 import connect
from flask import Flask, app, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TUT_SLUCHAINAYA_STROKA_IZ_KUCHI_SIMVOLOV'

@app.route('/')
def index():
    conn = get_db_connection()
    # выбираем все записи из таблицы posts
    posts = conn.execute('SELECT * FROM posts').fetchall()
    # все ещё не забываем обязательно закрывать соединение
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
# страница создания поста
@app.route('/create', methods=('GET','POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Не ввел заголовок!!!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?,?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

# страница редактирования поста
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)


# получаем конкретный пост
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone() # запятая после post_id - обязательно, иначе - ошибка unsupported type
    conn.close()
    if post is None:
        abort(404)
    return post

# метод для установки соединения с базой данных
def get_db_connection():
    # открываем соединение к файлу datatbase.db
    conn = sqlite3.connect('database.db')
    # устанавливаем row_factory в Row 
    # (чтобы получить доступ к столбцам на основе имен)
    conn.row_factory = sqlite3.Row
    # возвращаем объект подключения
    return conn