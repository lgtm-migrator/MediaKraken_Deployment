from common import common_global
from common import common_pagination_bootstrap
from sanic import Blueprint

blueprint_user_music = Blueprint('name_blueprint_user_music', url_prefix='/user')


@blueprint_user_music.route("/user_album_detail/<guid>")
@common_global.jinja_template.template('bss_user/media/bss_user_media_music_album_detail.html')
@common_global.auth.login_required
async def url_bp_user_album_detail(request, guid):
    """
    Display album detail page
    """
    return {}


@blueprint_user_music.route("/user_album_list")
@common_global.jinja_template.template('bss_user/user_music_album.html')
@common_global.auth.login_required
async def url_bp_user_album_list(request):
    """
    Display album page
    """
    page, offset = common_pagination_bootstrap.com_pagination_page_calc(request, user.per_page)
    media = []
    db_connection = await request.app.db_pool.acquire()
    for row_data in await request.app.db_functions.db_media_album_list(db_connection, offset,
                                                                       per_page,
                                                                       request.ctx.session[
                                                                           'search_text']):
        if 'mm_metadata_album_json' in row_data:
            media.append((row_data['mm_metadata_album_guid'], row_data['mm_metadata_album_name'],
                          row_data['mm_metadata_album_json']))
        else:
            media.append((row_data['mm_metadata_album_guid'],
                          row_data['mm_metadata_album_name'], None))
    request.ctx.session['search_page'] = 'music_album'
    pagination = Pagination(request,
                            total=await request.app.db_functions.db_media_album_count(db_connection,
                                                                                      request.ctx.session[
                                                                                          'search_page']),
                            record_name='music album(s)',
                            format_total=True,
                            format_number=True,
                            )

    await request.app.db_pool.release(db_connection)
    return {'media': media,
            'page': page,
            'per_page': per_page,
            'pagination': pagination,
            }
