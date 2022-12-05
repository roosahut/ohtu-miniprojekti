CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE book_references (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    author TEXT,
    title TEXT,
    year INTEGER,
    publisher TEXT
);