from app import db


def add_book(user, ref_key, author, title, publisher, year):
    try:
        sql = 'INSERT INTO books (user_id, ref_key, author, title, publisher, year) VALUES (:user, :ref_key, :author, :title, :publisher, :year)'
        db.session.execute(
            sql, {'user': user, 'ref_key': ref_key, 'author': author, 'title': title, 'publisher': publisher, 'year': year})
        db.session.commit()
        return True
    except:
        return False
    

def add_article(user, ref_key, author, title, journal, year, volume):
    try:
        sql = 'INSERT INTO articles (user_id, ref_key, author, title, journal, year, volume) VALUES (:user, :ref_key, :author, :title, :journal, :year, :volume)'
        db.session.execute(
            sql, {'user': user, 'ref_key': ref_key, 'author': author, 'title': title, 'journal': journal, 'year': year, 'volume': volume})
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
    
    
def add_inproceedings(user, ref_key, author, title, booktitle, year):
    try:
        sql = 'INSERT INTO inproceedings (user_id, ref_key, author, title, booktitle, year) VALUES (:user, :ref_key, :author, :title, :booktitle, :year)'
        db.session.execute(
            sql, {'user': user, 'ref_key': ref_key, 'author': author, 'title': title, 'booktitle': booktitle, 'year': year})
        db.session.commit()
        return True
    except:
        return False
    

def get_citations(user_id, type):
    type = type
    try:
        sql = f'SELECT * FROM {type} WHERE user_id=:user_id'
        citation = db.session.execute(sql, {'user_id': user_id}).fetchall()
        return citation       
    except:
        return False