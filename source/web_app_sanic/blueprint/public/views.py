# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""

import sys

sys.path.append('..')
import database as database_base
from MediaKraken.extensions import login_manager
from MediaKraken.public.forms import LoginForm
from MediaKraken.user.forms import RegisterForm
from MediaKraken.user.models import User
from MediaKraken.utils import flash_errors
from flask import Blueprint, request, render_template, flash, url_for, redirect, session
from flask_login import current_user
from flask_login import login_user, login_required, logout_user

# this fixes the login issue!!!!!!!!!!!!!!!!!!!!!!!!!
# blueprint = Blueprint('public', __name__, url_prefix='/public', static_folder="../static")
blueprint = Blueprint('public', __name__, static_folder="../static")


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@blueprint.route('/logout/')
@login_required
def logout():
    """
    Logout user and clear their session
    """
    logout_user()
    session.clear()
    flash('You are logged out.', 'info')
    return redirect(request.app.url_for('public.home'))


@blueprint.route("/register/", methods=['GET', 'POST'])
def register():
    """
    Display registration form
    """
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        admin_user = False
        # if first user set it as administrator
        db_connection = database_base.MKServerDatabase()
        db_connection.db_open()
        if db_connection.db_table_count('mm_user') == 0:
            admin_user = True
        db_connection.db_close()
        # add the user
        new_user = User.create(username=form.username.data,
                               email=form.email.data,
                               password=form.password.data,
                               active=True,
                               is_admin=admin_user)
        flash("Thank you for registering. You can now log in.", 'success')
        return redirect(request.app.url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)
