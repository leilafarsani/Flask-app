from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
def generate_secret_key():
    secret_key = secrets.token_hex(16)  # Generate a 32-character (16 bytes) hex secret key
    return secret_key

app.config['SECRET_KEY'] = 'your_secret_key_here'

from app import routes
