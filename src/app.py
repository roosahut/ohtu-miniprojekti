from flask import Flask, render_template, request, redirect, send_file
import string
from config import SECRET_KEY, DATABASE_URL
from db import db
import services.users as users
import services.references as ref


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db.init_app(app)


@app.get('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not users.login(username, password):
            return render_template('error.html', message='Wrong username or password')
        return redirect('/')


@app.route('/register', methods=['get', 'post'])
def reqister():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        username = request.form['username']
        if len(username) < 4:
            return render_template('error.html', message='Username is too short, it should be at least 4 characters long')
        characters = string.ascii_letters + string.digits + 'äåöÄÅÖ'
        for i in username:
            if i not in characters:
                return render_template('error.html', message='Username must have only letters and numbers in it')

        password1 = request.form['password1']
        password2 = request.form['password2']
        if password1 != password2:
            return render_template('error.html', message='The passwords are not the same')
        if len(password1) < 8:
            return render_template('error.html', message='Password is too short')

        if not users.register(username, password1):
            return render_template('error.html', message='The registration was unsuccesful, try a different username')

        return redirect('/')


@app.route('/add_reference', methods=['get', 'post'])
def add_refence():
    reference_type = {
        'book': 'book.html',
        'article': 'article.html',
        'master_thesis': 'master.html',
        'inproceedings': 'inproceedings.html'
    }
    if request.method == 'GET':
        ref_type = request.args['add_reference']
        return render_template(reference_type[ref_type])


@app.route('/add_book', methods=['get', 'post'])
def add_book():
    if request.method == "POST":
        ref_key = request.form['ref_key']
        if ref.find_refkey(users.user_id(), ref_key):
            return render_template('error.html', message='You already have a reference with this key.')
        author = request.form['author']
        title = request.form['title']
        publisher = request.form['publisher']
        year = request.form['year']

        if not ref.add_book(users.user_id(), ref_key, author, title, publisher, year):
            return render_template('error.html', message='Reference adding failed, try again')

        return redirect('/')


@app.route('/add_article', methods=['get', 'post'])
def add_article():
    if request.method == "POST":
        ref_key = request.form['ref_key']
        if ref.find_refkey(users.user_id(), ref_key):
            return render_template('error.html', message='You already have a reference with this key.')
        author = request.form['author']
        title = request.form['title']
        journal = request.form['journal']
        year = request.form['year']
        volume = request.form['volume']

        if not ref.add_article(users.user_id(), ref_key, author, title, journal, year, volume):
            return render_template('error.html', message='Reference adding failed, try again')

        return redirect('/')


@app.route('/add_masterthesis', methods=['get', 'post'])
def add_masterthesis():
    if request.method == "POST":
        ref_key = request.form['ref_key']
        if ref.find_refkey(users.user_id(), ref_key):
            return render_template('error.html', message='You already have a reference with this key.')
        author = request.form['author']
        title = request.form['title']
        school = request.form['school']
        year = request.form['year']

        if not ref.add_masterthesis(users.user_id(), ref_key, author, title, school, year):
            return render_template('error.html', message='Reference adding failed, try again')

        return redirect('/')


@app.route('/add_inproceedings', methods=['get', 'post'])
def add_inproceedings():
    if request.method == "POST":
        ref_key = request.form['ref_key']
        if ref.find_refkey(users.user_id(), ref_key):
            return render_template('error.html', message='You already have a reference with this key.')
        author = request.form['author']
        title = request.form['title']
        booktitle = request.form['booktitle']
        year = request.form['year']

        if not ref.add_inproceedings(users.user_id(), ref_key, author, title, booktitle, year):
            return render_template('error.html', message='Reference adding failed, try again')

        return redirect('/')


@app.route('/view_references', methods=['get', 'post'])
def view_references():
    if request.method == "GET":
        articles = ref.get_articles(users.user_id(),"", "")
        books = ref.get_books(users.user_id(), "", "")
        inproceedings = ref.get_inproceedings(users.user_id(), "", "")
        master_thesis = ref.get_master_thesis(users.user_id(), "", "")

        return render_template('view_references.html', articles=articles, books=books, inproceedings=inproceedings, master_thesis=master_thesis)
    
    if request.method == "POST":
        search = request.form['search']
        articles = ref.get_articles(users.user_id(),"", search)
        books = ref.get_books(users.user_id(), "", search)
        inproceedings = ref.get_inproceedings(users.user_id(), "", search)
        master_thesis = ref.get_master_thesis(users.user_id(), "", search)

        return render_template('view_references.html', articles=articles, books=books, inproceedings=inproceedings, master_thesis=master_thesis)


@app.route('/logout')
def logout():
    users.logout()

    return redirect('/')


@app.route('/view_bibtex', methods=['get', 'post'])
def view_bibtex():
    if request.method == "GET":
        articles = ref.get_articles(users.user_id(), "", "")
        books = ref.get_books(users.user_id(), "", "")
        inproceedings = ref.get_inproceedings(users.user_id(), "", "")
        master_thesis = ref.get_master_thesis(users.user_id(), "", "")

        return render_template('view_bibtex.html', articles=articles, books=books, inproceedings=inproceedings, master_thesis=master_thesis)


@app.post('/create_bibtex')
def create_bibtex():
    file_name = request.form['file_name']
    ref_keys = request.form.getlist("check")
    if len(ref_keys) == 0:
        return render_template('error.html', message='You have to choose at least one reference.')
    if not file_name:
        return render_template('error.html', message='You have to write the filename.')
    if not ref.add_references_to_file(users.user_id(), ref_keys):
        return render_template('error.html', message='Error creating the file.')
    download_name = f'{file_name}.bib'
    return send_file('bibtex.bib', download_name=download_name, as_attachment=True)

@app.route("/ping")
def ping():
    return "Pong"

@app.post('/tests/reset')
def reset():
    users.delete_all()
    ref.delete_all()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
