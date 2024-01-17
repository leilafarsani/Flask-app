from flask import render_template, request
from app import app, db
from app.models import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Example form handling logic
    name = request.form['name']
    # Additional logic to handle form data
    return 'Form submitted!'
