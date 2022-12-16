import os
from flask import session, abort, request
from werkzeug.security import check_password_hash, generate_password_hash
from app import db


def login(username, password):
    sql = 'SELECT id, password, username FROM users WHERE username=:username'
    result = db.session.execute(sql, {'username': username})
    user = result.fetchone()
    if not user:
        return False
    if check_password_hash(user[1], password):
        session['user_id'] = user[0]
        session['user_name'] = user[2]
        session['csrf_token'] = os.urandom(16).hex()
        return True


def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = 'INSERT INTO users (username, password) VALUES (:username, :password)'
        db.session.execute(
            sql, {'username': username, 'password': hash_value})
        db.session.commit()
        return login(username, password)
    except:
        return False


def user_id():
    return session.get('user_id', 0)


def logout():
    del session['user_id']
    del session['user_name']


def check_csrf():
    if session['csrf_token'] != request.form['csrf_token']:
        abort(403)


def delete_all():
    sql = 'TRUNCATE TABLE users CASCADE'
    db.session.execute(sql)
    db.session.commit()


def find_all():
    sql = 'SELECT * FROM users'
    users = db.session.execute(sql).fetchall()
    return users
