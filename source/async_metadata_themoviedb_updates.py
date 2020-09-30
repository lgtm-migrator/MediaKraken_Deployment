"""
  Copyright (C) 2016 Quinn D Granfor <spootdev@gmail.com>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License version 2 for more details.

  You should have received a copy of the GNU General Public License
  version 2 along with this program; if not, write to the Free
  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
"""

import asyncio
import json
import sys
import uuid

from common import common_config_ini
from common import common_global
from common import common_logging_elasticsearch_httpx
from common import common_network_async
from common import common_signal
from common import common_system


async def main(loop):
    # start logging
    common_logging_elasticsearch_httpx.com_es_httpx_post_async(message_type='info',
                                                               message_text='START',
                                                               index_name='async_metadata_themoviedb_updates')

    # set signal exit breaks
    common_signal.com_signal_set_break()

    # open the database
    option_config_json, db_connection = \
        await common_config_ini.com_config_read_async(loop=loop,
                                                      as_pool=False)

    # TODO this should go through the limiter
    # process movie changes
    new_movie_data = json.loads(await common_network_async.mk_network_fetch_from_url_async(
        'https://api.themoviedb.org/3/movie/changes'
        '?api_key=%s' % option_config_json['API']['themoviedb']))['id']
    for movie_change in new_movie_data['results']:
        common_logging_elasticsearch_httpx.com_es_httpx_post_async(message_type='info',
                                                                   message_text={
                                                                       'mov': movie_change['id']})
        # verify it's not already in the database
        if db_connection.db_meta_guid_by_tmdb(str(movie_change['id']),
                                              db_connection=db_connection) is None:
            # verify there is not a dl que for this record
            dl_meta = db_connection.db_download_que_exists(None,
                                                           common_global.DLMediaType.Movie.value,
                                                           'themoviedb',
                                                           str(movie_change['id']),
                                                           db_connection=db_connection)
            common_logging_elasticsearch_httpx.com_es_httpx_post_async(message_type='info',
                                                                       message_text={
                                                                           'dl_meta': dl_meta})
            if dl_meta is None:
                db_connection.db_download_insert(provider='themoviedb',
                                                 que_type=common_global.DLMediaType.Movie.value,
                                                 down_json=json.dumps({'Status': 'Fetch',
                                                                       'ProviderMetaID': str(
                                                                           movie_change['id'])}),
                                                 down_new_uuid=uuid.uuid4(),
                                                 db_connection=db_connection
                                                 )
        else:
            # it's on the database, so must update the record with latest information
            db_connection.db_download_insert(provider='themoviedb',
                                             que_type=common_global.DLMediaType.Movie.value,
                                             down_json=json.dumps({'Status': 'Update',
                                                                   'ProviderMetaID': str(
                                                                       movie_change['id'])}),
                                             down_new_uuid=uuid.uuid4(),
                                             db_connection=db_connection
                                             )
    # TODO this should go through the limiter
    # process tv changes
    new_tv_data = json.loads(await common_network_async.mk_network_fetch_from_url_async(
        'https://api.themoviedb.org/3/tv/changes'
        '?api_key=%s' % option_config_json['API']['themoviedb']))['id']
    for tv_change in new_tv_data['results']:
        common_logging_elasticsearch_httpx.com_es_httpx_post_async(message_type='info',
                                                                   message_text={
                                                                       'stuff': "tv: %s" %
                                                                                tv_change['id']})
        # verify it's not already in the database
        if db_connection.db_metatv_guid_by_tmdb(str(tv_change['id']),
                                                db_connection=db_connection) is None:
            dl_meta = db_connection.db_download_que_exists(None, common_global.DLMediaType.TV.value,
                                                           'themoviedb', str(tv_change['id']),
                                                           db_connection=db_connection)
            if dl_meta is None:
                db_connection.db_download_insert(provider='themoviedb',
                                                 que_type=common_global.DLMediaType.TV.value,
                                                 down_json=json.dumps({'Status': 'Fetch',
                                                                       'ProviderMetaID': str(
                                                                           tv_change['id'])}),
                                                 down_new_uuid=uuid.uuid4(),
                                                 db_connection=db_connection
                                                 )
        else:
            # it's on the database, so must update the record with latest information
            db_connection.db_download_insert(provider='themoviedb',
                                             que_type=common_global.DLMediaType.TV.value,
                                             down_json=json.dumps({'Status': 'Update',
                                                                   'ProviderMetaID': str(
                                                                       tv_change['id'])}),
                                             down_new_uuid=uuid.uuid4(),
                                             db_connection=db_connection
                                             )

    # commit all changes
    db_connection.db_commit(db_connection=db_connection)

    # close DB
    db_connection.db_close(db_connection=db_connection)


if __name__ == "__main__":
    # verify this program isn't already running!
    if common_system.com_process_list(
            process_name='/usr/bin/python3 /mediakraken/async_metadata_themoviedb_updates.py'):
        sys.exit(0)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
