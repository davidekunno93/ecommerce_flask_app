from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import RegisterForm, LoginForm
from ..models import User
from ..myfunctions import Amiibo
from flask_login import current_user, login_user, logout_user
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate:
            un = form.username.data
            pw = form.password.data
            user = User.query.filter_by(username=un).first()
            if user:
                if user.password == pw:
                    login_user(user)
                    print("You've successfully logged in!")
                else:
                    print("Wrong password. Try again")
            else:
                print("There is no user with this username")
            return redirect(url_for('products_land'), )
    return render_template('login.html', login_form=form)

@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate:
            un = form.username.data.lower()
            em = form.email.data.lower()
            pw = form.password.data.lower()
            user = User(un, em, pw)
            user.save_user()
            return redirect(url_for('auth.login'))

    return render_template('signup.html', register_form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))