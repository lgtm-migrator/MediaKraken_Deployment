from common import common_global
from python_paginate.web.sanic_paginate import Pagination
from sanic import Blueprint

blueprint_user_periodical = Blueprint('name_blueprint_user_periodical', url_prefix='/user')


@blueprint_user_periodical.route('/periodical', methods=['GET'])
@common_global.jinja_template.template('user/user_periodical.html')
@common_global.auth.login_required
async def url_bp_user_periodical_list(request):
    """
    Display periodical page
    """
    page, per_page, offset = Pagination.get_page_args(request)
    request['session']['search_page'] = 'media_periodicals'
    db_connection = await request.app.db_pool.acquire()
    pagination = Pagination(request,
                            total=await request.app.db_functions.db_media_book_list_count(
                                db_connection,
                                request['session']['search_text']),
                            record_name='periodical(s)',
                            format_total=True,
                            format_number=True,
                            )
    media_data = await request.app.db_functions.db_media_book_list(db_connection, offset, per_page,
                                                                   request['session'][
                                                                       'search_text'])
    await request.app.db_pool.release(db_connection)
    return {
        'media': media_data,
        'page': page,
        'per_page': per_page,
        'pagination': pagination,
    }


@blueprint_user_periodical.route('/periodical_detail/<guid>', methods=['GET'])
@common_global.jinja_template.template('user/user_periodical_detail.html')
@common_global.auth.login_required
async def url_bp_user_periodical_detail(request, guid):
    """
    Display periodical detail page
    """
    return {}
