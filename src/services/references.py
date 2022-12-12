from app import db
import services.bibtex as bibtex


def add_article(user, ref_key, author, title, journal, year, volume):
    try:
        sql = 'INSERT INTO articles (user_id, ref_key, author, title, journal, year, volume) VALUES (:user, :ref_key, :author, :title, :journal, :year, :volume)'
        db.session.execute(
            sql, {'user': user, 'ref_key': ref_key, 'author': author, 'title': title, 'journal': journal, 'year': year, 'volume': volume})
        db.session.commit()
        return True
    except:
        return False


def add_book(user, ref_key, author, title, publisher, year):
    try:
        sql = 'INSERT INTO books (user_id, ref_key, author, title, publisher, year) VALUES (:user, :ref_key, :author, :title, :publisher, :year)'
        db.session.execute(
            sql, {'user': user, 'ref_key': ref_key, 'author': author, 'title': title, 'publisher': publisher, 'year': year})
        db.session.commit()
        return True
    except:
        return False


def add_inproceedings(user, ref_key, author, title, booktitle, year):
    try:
        sql = 'INSERT INTO inproceedings (user_id, ref_key, author, title, booktitle, year) VALUES (:user, :ref_key, :author, :title, :booktitle, :year)'
        db.session.execute(
            sql, {'user': user, 'ref_key': ref_key, 'author': author, 'title': title, 'booktitle': booktitle, 'year': year})
        db.session.commit()
        return True
    except:
        return False


def add_masterthesis(user, ref_key, author, title, school, year):
    try:
        sql = 'INSERT INTO masterthesis (user_id, ref_key, author, title, school, year) VALUES (:user, :ref_key, :author, :title, :school, :year)'
        db.session.execute(
            sql, {'user': user, 'ref_key': ref_key, 'author': author, 'title': title, 'school': school, 'year': year})
        db.session.commit()
        return True
    except:
        return False


def get_articles(user_id):
    try:
        sql = 'SELECT * FROM articles WHERE user_id=:user_id'
        articles = db.session.execute(sql, {'user_id': user_id}).fetchall()
        return articles
    except:
        return False


def get_books(user_id):
    try:
        sql = 'SELECT * FROM books WHERE user_id=:user_id'
        books = db.session.execute(sql, {'user_id': user_id}).fetchall()
        return books
    except:
        return False


def get_inproceedings(user_id):
    try:
        sql = 'SELECT * FROM inproceedings WHERE user_id=:user_id'
        inproceedings = db.session.execute(
            sql, {'user_id': user_id}).fetchall()
        return inproceedings
    except:
        return False


def get_master_thesis(user_id):
    try:
        sql = 'SELECT * FROM masterthesis WHERE user_id=:user_id'
        masterthesis = db.session.execute(sql, {'user_id': user_id}).fetchall()
        return masterthesis
    except:
        return False


def delete_all():
    sql = 'TRUNCATE TABLE articles CASCADE'
    db.session.execute(sql)
    sql = 'TRUNCATE TABLE books CASCADE'
    db.session.execute(sql)
    sql = 'TRUNCATE TABLE inproceedings CASCADE'
    db.session.execute(sql)
    sql = 'TRUNCATE TABLE masterthesis CASCADE'
    db.session.execute(sql)
    db.session.commit()


def get_bibtex(user_id):
    books = get_books(user_id)
    bibtex_list = []
    for book in books:
        bibtex_list.append(bibtex.book_to_bibtex(book))
    return bibtex_list
