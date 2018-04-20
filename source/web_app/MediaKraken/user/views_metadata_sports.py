"""
User view in webapp
"""
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Blueprint, render_template, g, request
from flask_login import login_required

blueprint = Blueprint("user_metadata_sports", __name__, url_prefix='/users',
                      static_folder="../static")
import sys

sys.path.append('..')
sys.path.append('../..')
from common import common_config_ini
from common import common_pagination
import database as database_base
from MediaKraken.user.forms import SearchForm

option_config_json, db_connection = common_config_ini.com_config_read()


@blueprint.route('/meta_sports_list', methods=['GET', 'POST'])
@blueprint.route('/meta_sports_list/', methods=['GET', 'POST'])
@login_required
def metadata_sports_list():
    """
    Display sports metadata list
    """
    page, per_page, offset = common_pagination.get_page_items()
    media = []
    form = SearchForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            pass
        mediadata = g.db_connection.db_meta_sports_list(offset, per_page,
                                                        request.form['search_text'])
    else:
        mediadata = g.db_connection.db_meta_sports_list(offset, per_page)

    pagination = common_pagination.get_pagination(page=page,
                                                  per_page=per_page,
                                                  total=g.db_connection.db_meta_sports_list_count(),
                                                  record_name='sporting events',
                                                  format_total=True,
                                                  format_number=True,
                                                  )
    return render_template('users/metadata/meta_sports_list.html', form=form,
                           media_sports_list=mediadata,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@blueprint.route('/meta_sports_detail/<guid>/')
@blueprint.route('/meta_sports_detail/<guid>')
@login_required
def metadata_sports_detail(guid):
    """
    Display sports detail metadata
    """
    return render_template('users/metadata/meta_sports_detail.html', guid=guid,
                           data=g.db_connection.db_meta_sports_by_guid(guid))


@blueprint.before_request
def before_request():
    """
    Executes before each request
    """
    g.db_connection = database_base.MKServerDatabase()
    g.db_connection.db_open()


@blueprint.teardown_request
def teardown_request(exception):  # pylint: disable=W0613
    """
    Executes after each request
    """
    g.db_connection.db_close()
