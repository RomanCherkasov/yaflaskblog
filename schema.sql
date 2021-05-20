DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- поле id автоматически увеличивающееся (первичный ключ)
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- полле created с текущим временем
    title TEXT NOT NULL, -- поле title с заголовком
    content TEXT NOT NULL -- поле content с содержанием поста
);