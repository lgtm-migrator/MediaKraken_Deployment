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

import json

from common import common_global
from common import common_metadata_provider_thegamesdb

THEGAMESDB_CONNECTION = common_metadata_provider_thegamesdb.CommonMetadataGamesDB()


def game_system_update():
    data = THEGAMESDB_CONNECTION.com_meta_gamesdb_platform_list()[
        'Data']['Platforms']['Platform']
    print((type(data)), flush=True)
    print(data, flush=True)
    for game_system in data:
        print(game_system, flush=True)
        game_sys_detail = \
            THEGAMESDB_CONNECTION.com_meta_gamesdb_platform_by_id(game_system['id'])['Data'][
                'Platform']
        print((type(game_sys_detail)), flush=True)
        print(game_sys_detail, flush=True)
        break


def metadata_game_lookup(db_connection, download_que_json, download_que_id):
    """
    Lookup game metadata
    """
    metadata_uuid = None  # so not found checks verify later
    common_global.es_inst.com_elastic_index('info', {'game filename': download_que_json['Path']})
    # TODO determine short name/etc
    for row_data in db_connection.db_meta_game_by_name(download_que_json['Path']):
        # TODO handle more than one match
        metadata_uuid = row_data['gi_id']
        break
    common_global.es_inst.com_elastic_index('info', {"meta game metadata_uuid B": metadata_uuid})
    if metadata_uuid is None:
        # no matches by name
        # search giantbomb since not matched above via DB or nfo/xml
        download_que_json.update({'Status': 'Search'})
        # save the updated status
        db_connection.db_begin()
        db_connection.db_download_update(json.dumps(download_que_json),
                                         download_que_id)
        # set provider last so it's not picked up by the wrong thread
        db_connection.db_download_update_provider('giantbomb', download_que_id)
        db_connection.db_commit()
    return metadata_uuid
