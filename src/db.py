from flask_sqlalchemy import SQLAlchemy
from app import app
from config import DATABASE_URL

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
