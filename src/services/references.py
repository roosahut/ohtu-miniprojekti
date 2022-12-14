import os
from app import db
import services.bibtex_format as bibtex_format


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


def get_articles(user_id, ref_key, search):
    try:
        sql = 'SELECT * FROM articles WHERE user_id=:user_id AND ref_key LIKE :ref_key AND title LIKE :search OR ref_key LIKE :search OR author LIKE :search OR journal LIKE :search'
        articles = db.session.execute(
            sql, {'user_id': user_id, 'ref_key':'%' + ref_key + '%', 'search':'%' + search + '%'}).fetchall()
        return articles
    except:
        return False


def get_books(user_id, ref_key, search):
    try:
        sql = 'SELECT * FROM books WHERE user_id=:user_id AND ref_key LIKE :ref_key AND title LIKE :search OR ref_key LIKE :search OR author LIKE :search OR publisher LIKE :search'
        books = db.session.execute(
            sql, {'user_id': user_id, 'ref_key':'%' + ref_key + '%', 'search':'%' + search + '%'}).fetchall()
        return books
    except:
        return False


def get_inproceedings(user_id, ref_key, search):
    try:
        sql = 'SELECT * FROM inproceedings WHERE user_id=:user_id AND ref_key LIKE :ref_key AND title LIKE :search OR ref_key LIKE :search OR author LIKE :search OR booktitle LIKE :search'
        inproceedings = db.session.execute(
            sql, {'user_id': user_id, 'ref_key':'%' + ref_key + '%', 'search':'%' + search + '%'}).fetchall()
        return inproceedings
    except:
        return False


def get_master_thesis(user_id, ref_key, search):
    try:
        sql = 'SELECT * FROM masterthesis WHERE user_id=:user_id AND ref_key LIKE :ref_key AND title LIKE :search OR ref_key LIKE :search OR author LIKE :search OR school LIKE :search'
        masterthesis = db.session.execute(
            sql, {'user_id': user_id, 'ref_key':'%' + ref_key + '%', 'search':'%' + search + '%'}).fetchall()
        return masterthesis
    except:
        return False


def check_refkey(user_id, refkey, type):
    try:
        sql = f'SELECT * FROM {type} WHERE ref_key=:refkey AND user_id=:user_id'
        reference = db.session.execute(
            sql, {'refkey': refkey, 'user_id': user_id}).fetchall()
        return reference
    except:
        return False


def find_refkey(user_id, refkey):
    if check_refkey(user_id, refkey, 'books'):
        return True
    elif check_refkey(user_id, refkey, 'articles'):
        return True
    elif check_refkey(user_id, refkey, 'masterthesis'):
        return True
    elif check_refkey(user_id, refkey, 'inproceedings'):
        return True
    else:
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


def get_bibtex_forms(user_id, ref_keys):
    bibtex_list = []

    for reference in ref_keys:
        articles = get_articles(user_id, reference, '')
        for article in articles:
            bibtex_list.append(bibtex_format.article_to_bibtex(article))
            
        books = get_books(user_id, reference, '')
        for book in books:
            bibtex_list.append(bibtex_format.book_to_bibtex(book))

        inproceedings = get_inproceedings(user_id, reference, '')
        for inproceeding in inproceedings:
            bibtex_list.append(
                bibtex_format.inproceedings_to_bibtex(inproceeding))

        masterthesis = get_master_thesis(user_id, reference, '')
        for thesis in masterthesis:
            bibtex_list.append(bibtex_format.masterthesis_to_bibtex(thesis))

    return bibtex_list


def add_references_to_file(user_id, ref_keys):
    try:
        if os.path.exists('src/bibtex.bib'):
            os.remove('src/bibtex.bib')
        file = open('src/bibtex.bib', 'a')
        bibtex_form = get_bibtex_forms(user_id, ref_keys)
        for i in bibtex_form:
            for row in i:
                file.write(row)
                file.write("\n")
        return True
    except:
        return False
