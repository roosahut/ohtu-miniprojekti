CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    ref_key TEXT UNIQUE,
    author TEXT,
    title TEXT,
    publisher TEXT,
    year INTEGER
);

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    ref_key TEXT UNIQUE,
    author TEXT,
    title TEXT,
    journal TEXT,
    year INTEGER,
    volume INTEGER
);

CREATE TABLE inproceedings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    ref_key TEXT UNIQUE,
    author TEXT,
    title TEXT,
    booktitle TEXT,
    year INTEGER
);

CREATE TABLE masterthesis (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    ref_key TEXT UNIQUE,
    author TEXT,
    title TEXT,
    school TEXT,
    year INTEGER
);
