# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from MediaKraken.user.models import User
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append('Unknown username')
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        if not self.user.active:
            self.username.errors.append('User not activated')
            return False
        return True


# class SearchForm(Form):
#     """
#     for searching media
#     """
#     search_text = TextField(
#         'Search For')  # , validators=[DataRequired(), Length(min=1, max=255)])  # remove required due to browse buttons
#
#     def __init__(self, *args, **kwargs):
#         super(SearchForm, self).__init__(*args, **kwargs)
#
#     def validate(self):
#         initial_validation = super(SearchForm, self).validate()
#         if not initial_validation:
#             return False
#         return True
