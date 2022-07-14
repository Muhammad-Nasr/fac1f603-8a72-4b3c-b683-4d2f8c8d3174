
from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from app import db, login_manager
from app.authentication import bp
from app.authentication.forms import LoginForm, RegisterationForm
from app.authentication.models import User

from app.authentication.util import verify_pass

# Login & Registration


@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))

    if login_form.validate_on_submit():
            # read form data
        username = request.form['username']
        password = request.form['password']
        print(username, password)

                # Locate user
        user = User.query.filter_by(username=username).first()

            # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            print(current_user)
            print('good one')
            return redirect(url_for('home.index'))

        return render_template('accounts/login.html',
                               msg='wrong credentials',
                                   form=login_form)

            # Something (user or pass) is not ok
    return render_template('accounts/login.html',
                           form=login_form)




@bp.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = RegisterationForm()
    if create_account_form.validate_on_submit():

        username = request.form['username']
        email = request.form['email']
        print(username, email)

        # Check usename exists
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already Exist, Please Choose another one',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    else:
        return render_template('accounts/register.html', form=create_account_form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


