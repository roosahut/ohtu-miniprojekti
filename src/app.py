import re
from flask import Flask, render_template, request, redirect
import string
from config import SECRET_KEY, DATABASE_URL
from db import db
import services.users as users

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
        pattern = re.compile(r'[^\w\dåäöÅÄÖ]')
        if not pattern.search(username):
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
    if request.method == 'POST':
        'tänne ehkä lomakkeiden tietoja'


@app.route('/get_references', methods=['get', 'post'])
def get_references():
    return redirect('/')


@app.route('/logout')
def logout():
    users.logout()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
