

@blueprint.route("/album_list")
@login_required
def user_album_list_page():
    """
    Display album page
    """
    page, per_page, offset = common_pagination.get_page_items()
    media = []
    for row_data in g.db_connection.db_media_album_list(offset, per_page, session['search_text']):
        if 'mm_metadata_album_json' in row_data:
            media.append((row_data['mm_metadata_album_guid'], row_data['mm_metadata_album_name'],
                          row_data['mm_metadata_album_json']))
        else:
            media.append((row_data['mm_metadata_album_guid'],
                          row_data['mm_metadata_album_name'], None))
    session['search_page'] = 'music_album'
    pagination = common_pagination.get_pagination(page=page,
                                                  per_page=per_page,
                                                  total=g.db_connection.db_media_album_count(
                                                      session['search_page']),
                                                  record_name='music album(s)',
                                                  format_total=True,
                                                  format_number=True,
                                                  )
    return render_template("users/user_music_album_page.html", media=media,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@blueprint.route("/album_detail/<guid>")
@login_required
def user_album_detail_page(guid):
    """
    Display album page
    """
    pass

