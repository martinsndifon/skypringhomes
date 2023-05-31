#!/usr/bin/python3
"""Authentication module"""

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from web_dynamic_admin.views import auth
from werkzeug.security import check_password_hash
from models.admin import Admin
from models import storage


@auth.route('/login')
def login():
    """Handles admin login"""
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    """Handles the login form submission"""
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    admin = storage.get_email(Admin, email)

    # check if the admin user exists
    if not admin or not check_password_hash(admin.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    # if password is correct, redirect admin user to admin home page
    login_user(admin, remember=remember)
    return redirect(url_for('app_views.properties_admin'))

@auth.route('/logout')
@login_required
def logout():
    """logs out the admin user and close the session"""
    logout_user()
    # returns to the login screen for now
    return redirect(url_for('auth.login'))
