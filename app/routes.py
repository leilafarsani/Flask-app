from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']

    # Check if username already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        # Handle the case where the username already exists
        return "Username already taken. Please choose a different username."

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100  # Convert cm to meters
    bmi = round(weight / (height ** 2), 2)
    
    return render_template('bmi_result.html', bmi=bmi)
