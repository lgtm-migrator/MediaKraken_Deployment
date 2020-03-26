import json


async def db_metadata_search(self, db_connection, search_string, search_type='Local',
                             search_movie=True,
                             search_tvshow=True,
                             search_album=True,
                             search_image=True,
                             search_publication=True,
                             search_game=True):
    """
    search media local, remote and metadata providers
    """
    json_return_data = {}
    if search_type == 'Local':
        if search_movie:
            # movie section
            json_return_data['Movie'] = json.dumps(
                await db_connection.fetch('SELECT mm_metadata_guid,'
                                          ' mm_media_name, '
                                          'similarity(mm_media_name, %s) AS sml'
                                          ' FROM mm_metadata_movie'
                                          ' WHERE mm_media_name % %s'
                                          ' ORDER BY sml DESC, LOWER(mm_media_name);',
                                          (search_string,
                                           search_string)))
        if search_tvshow:
            # tv show section
            json_return_data['TVShow'] = json.dumps(
                await db_connection.fetch('SELECT mm_metadata_tvshow_guid,'
                                          ' mm_metadata_tvshow_name,'
                                          ' similarity(mm_metadata_tvshow_name, %s) AS sml'
                                          ' FROM mm_metadata_tvshow'
                                          ' WHERE mm_metadata_tvshow_name % %s'
                                          ' ORDER BY sml DESC, LOWER(mm_metadata_tvshow_name);',
                                          (search_string, search_string)))
        if search_album:
            # album section
            json_return_data['Album'] = json.dumps(
                await db_connection.fetch('SELECT mm_metadata_album_guid,'
                                          ' mm_metadata_album_name,'
                                          ' similarity(mm_metadata_album_name, %s) AS sml'
                                          ' FROM mm_metadata_album'
                                          ' WHERE mm_metadata_album_name % %s'
                                          ' ORDER BY sml DESC, LOWER(mm_metadata_album_name);',
                                          (search_string, search_string)))
        if search_image:
            # TODO image search
            pass
        if search_publication:
            # publication section
            json_return_data['Publication'] = json.dumps(
                await db_connection.fetch('SELECT mm_metadata_book_guid,'
                                          ' mm_metadata_book_name,'
                                          ' similarity(mm_metadata_book_name, %s) AS sml'
                                          ' FROM mm_metadata_book'
                                          ' WHERE mm_metadata_book_name % %s'
                                          ' ORDER BY sml DESC, LOWER(mm_metadata_book_name);',
                                          (search_string, search_string)))
        if search_game:
            # game section
            json_return_data['Game'] = json.dumps(await db_connection.fetch('SELECT gi_id,'
                                                                            ' gi_game_info_name,'
                                                                            ' similarity(gi_game_info_name, %s) AS sml'
                                                                            ' FROM mm_metadata_game_software_info'
                                                                            ' WHERE gi_game_info_name % %s'
                                                                            ' ORDER BY sml DESC, LOWER(gi_game_info_name);',
                                                                            (search_string,
                                                                             search_string)))
    return json_return_data
