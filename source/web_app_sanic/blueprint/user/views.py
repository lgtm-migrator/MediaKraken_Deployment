@blueprint.route('/movie_status/<guid>/<event_type>', methods=['GET', 'POST'])
@login_required
async def url_bp_user_movie_status(request, guid, event_type):
    """
    Set media status for specified media, user
    """
    common_global.es_inst.com_elastic_index('info', {'movie status': guid, 'event': event_type})
    if event_type == "sync":
        return redirect(request.app.url_for('user.sync_edit', guid=guid))
    else:
        if event_type == "mismatch":
            # TODO ummmm, how do I know which specific media to update?
            # TODO as some might be right
            g.db_connection.db_media_status_update(
                g.db_connection.db_metadata_from_media_guid(guid),
                current_user.get_id(), event_type)
            return json.dumps({'status': 'OK'})
        else:
            # g.db_connection.db_media_rating_update(
            #     guid, current_user.get_id(), event_type)
            g.db_connection.db_meta_movie_status_update(
                g.db_connection.db_metadata_from_media_guid(guid),
                current_user.get_id(), event_type)
            return json.dumps({'status': 'OK'})


@blueprint.route('/movie_metadata_status/<guid>/<event_type>', methods=['GET', 'POST'])
@login_required
async def url_bp_user_movie_metadata_status(request, guid, event_type):
    """
    Set media status for specified media, user
    """
    common_global.es_inst.com_elastic_index('info', {'movie metadata status': guid,
                                                     'event': event_type})
    g.db_connection.db_meta_movie_status_update(
        guid, current_user.get_id(), event_type)
    return json.dumps({'status': 'OK'})


@blueprint.route('/tv_status/<guid>/<event_type>', methods=['GET', 'POST'])
@login_required
async def url_bp_user_tv_status(request, guid, event_type):
    """
    Set media status for specified media, user
    """
    common_global.es_inst.com_elastic_index('info', {'tv status': guid, 'event': event_type})
    if event_type == "watched":
        pass
    elif event_type == "sync":
        pass
    elif event_type == "favorite":
        pass
    elif event_type == "poo":
        pass
    elif event_type == "mismatch":
        pass
    return redirect(request.app.url_for('user_tv.user_tv_page'))
