'''
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
'''

from __future__ import absolute_import, division, print_function, unicode_literals
import logging # pylint: disable=W0611
import json
import locale
locale.setlocale(locale.LC_ALL, '')
from common import common_config_ini
from common import common_logging
from common import common_metadata_tvmaze
from common import common_signal


# set signal exit breaks
common_signal.com_signal_set_break()


# start logging
common_logging.com_logging_start('./log/MediaKraken_Subprogram_tvmaze_Updates')


# open the database
config_handle, option_config_json, db_connection = common_config_ini.com_config_read()


# log start
db_connection.db_activity_insert('MediaKraken_Server tvmaze Update Start', None,\
    'System: Server tvmaze Start', 'ServerthetvmazeStart', None, None, 'System')


# grab updated show list with epoc data
tvshow_updated = 0
tvshow_inserted = 0
tvmaze = common_metadata_tvmaze.CommonMetadatatvmaze()
result = tvmaze.com_meta_tvmaze_show_updated()
#for show_list_json in result:
result = json.loads(result)
for tvmaze_id, tvmaze_time in result.items():
    logging.info("id: %s", tvmaze_id)
    # check to see if allready downloaded
    results = db_connection.db_metatv_guid_by_tvmaze(str(tvmaze_id))
    if results is not None:
        # if show was updated since db record
        # TODO if results['updated'] < tvmaze_time:
        #update_insert_show(tvmaze_id, results[0]) # update the guid
        logging.info("update")
        tvshow_updated += 1
    else:
        if db_connection.db_download_que_exists(None, 'tvmaze', tvmaze_id) is None:
            # insert new record as it's a new show
            db_connection.db_download_insert('tvmaze', json.dumps({'Status': 'Fetch',\
                'ProviderMetaID': tvmaze_id}))
            tvshow_inserted += 1


# log end
db_connection.db_activity_insert('MediaKraken_Server tvmaze Update Stop', None,\
    'System: Server tvmaze Stop', 'ServerthetvmazeStop', None, None, 'System')


# send notications
if tvshow_updated > 0:
    db_connection.db_notification_insert(locale.format('%d', tvshow_updated, True)\
        + " TV show(s) metadata updated.", True)
if tvshow_inserted > 0:
    db_connection.db_notification_insert(locale.format('%d', tvshow_inserted, True)\
        + " TV show(s) metadata added.", True)


# commit all changes to db
db_connection.db_commit()


# vaccum tables that had records added
db_connection.db_pgsql_vacuum_table('mm_metadata_tvshow')


# close DB
db_connection.db_close()