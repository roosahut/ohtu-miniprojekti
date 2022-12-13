from db import db
from app import app

app = app
app.app_context().push()


def create_tables():
    db.session.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
        
        CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            ref_key TEXT,
            author TEXT,
            title TEXT,
            publisher TEXT,
            year INTEGER
        );
        
        CREATE TABLE articles (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            ref_key TEXT,
            author TEXT,
            title TEXT,
            journal TEXT,
            year INTEGER,
            volume INTEGER
        );
        
        CREATE TABLE inproceedings (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            ref_key TEXT,
            author TEXT,
            title TEXT,
            booktitle TEXT,
            year INTEGER
        );

        CREATE TABLE masterthesis (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            ref_key TEXT,
            author TEXT,
            title TEXT,
            school TEXT,
            year INTEGER
        );
    """)
    
    db.session.commit()


def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS users CASCADE;
        DROP TABLE IF EXISTS books CASCADE;
        DROP TABLE IF EXISTS articles CASCADE;
        DROP TABLE IF EXISTS inproceedings CASCADE;
        DROP TABLE IF EXISTS masterthesis CASCADE;
    """)

    db.session.commit()


def initialize_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    initialize_database()