from flask import request, render_template, flash, redirect, url_for, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.extenshions import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        role = request.form.get('role')

        if not all([username, email, password, confirm_password, role]):
            flash("All fields are required", "danger")
            return redirect(url_for('auth.register'))

        if User.query.filter_by(email=email).first():
            flash("Email already exists", "danger")
            return redirect(url_for('auth.register'))

        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return redirect(url_for('auth.register'))

        if not email.endswith('@gmail.com'):
            flash("Email must end with @gmail.com", "danger")
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password,
            role=role
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please log in.", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Email not found. Please register first.", "danger")
            return redirect(url_for('auth.login'))

        if not check_password_hash(user.password, password):
            flash("Incorrect password. Please try again.", "danger")
            return redirect(url_for('auth.login'))

        login_user(user)
        flash("Logged in successfully!", "success")
        return redirect(url_for('main.dashboard'))

    return render_template('login.html')


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out successfully.", "info")
    return redirect(url_for("auth.login"))
