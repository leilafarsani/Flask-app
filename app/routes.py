from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User
from app.forms import LoginForm
from app.forms import RegistrationForm
import bcrypt



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
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Handle authentication here (e.g., check username and password)
        # If authentication is successful, redirect to a protected page
        # If authentication fails, display an error message
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Check if username already exists
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already taken. Please choose a different username.', 'danger')
            return redirect(url_for('register'))

        # Check if email already exists
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash('Email already taken. Please choose a different email.', 'danger')
            return redirect(url_for('register'))

        if form.password.data != form.confirm_password.data:
            flash('Password and Confirm Password must match.', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)  # Set the password using your hash_password function
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

# Function for checking a password
def check_password(candidate_password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, candidate_password)


from flask import Flask, render_template




