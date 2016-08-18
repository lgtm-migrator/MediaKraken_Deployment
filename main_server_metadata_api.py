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
# pull in the ini file config
import ConfigParser
config_handle = ConfigParser.ConfigParser()
config_handle.read("MediaKraken.ini")
import json
import uuid
import sys
import subprocess
import signal
import os
import time
import datetime
try:
    import cPickle as pickle
except:
    import pickle
import database as database_base
import metadata_anime
import metadata_game
import metadata_identification
import metadata_movie
import metadata_music_video
import metadata_music
import metadata_periodicals
import metadata_person
import metadata_sports
import metadata_tv
from common import common_file
from common import common_Hash
from common import common_isbndb
from com_meta_Limiter import *
from common import common_logging
from common import common_metadata
from common import common_metadata_imvdb
from common import common_metadata_limiter
from common import common_metadata_musicbrainz
from common import common_metadata_netflixroulette
from common import common_metadata_omdb
from common import common_metadata_pitchfork
from common import common_metadata_theaudiodb
from common import common_metadata_thegamesdb
from common import common_metadata_thelogodb
from common import common_metadata_thesportsdb
from common import common_metadata_thetvdb
from common import common_metadata_tmdb
from common import common_metadata_tv_intro
from common import common_metadata_tv_theme
from common import common_metadata_tvmaze
from common import common_network
from common import common_system
from common import common_thetvdb
from concurrent import futures
import locale
locale.setlocale(locale.LC_ALL, '')


def signal_receive(signum, frame):
    print('CHILD Main Metadata: Received USR1')
    # os.kill(proc_trigger.pid, signal.SIGTERM)
    # cleanup db
    db.srv_db_rollback()
    # log stop
    db.srv_db_activity_insert('MediaKraken_Metadata API Stop', None,\
        'System: Metadata API Stop', 'ServerMetadataAPIStop', None, None, 'System')
    db.srv_db_close()
    sys.stdout.flush()
    sys.exit(0)


# store pid for initd
pid = os.getpid()
op = open("/var/mm_server_metadata_api.pid", "w")
op.write("%s" % pid)
op.close()


# start logging
common_logging.com_logging_start('./log/MediaKraken_Metadata_API')


# open the database
db = database_base.MKServerDatabase()
db.srv_db_open(config_handle.get('DB Connections', 'PostDBHost').strip(),\
    config_handle.get('DB Connections', 'PostDBPort').strip(),\
    config_handle.get('DB Connections', 'PostDBName').strip(),\
    config_handle.get('DB Connections', 'PostDBUser').strip(),\
    config_handle.get('DB Connections', 'PostDBPass').strip())


db.srv_db_activity_insert('MediaKraken_Metadata API Start', None,\
     'System: Metadata API Start', 'ServerMetadataAPIStart', None, None, 'System')


if str.upper(sys.platform[0:3]) == 'WIN' or str.upper(sys.platform[0:3]) == 'CYG':
    signal.signal(signal.SIGBREAK, signal_receive)   # ctrl-c
else:
    signal.signal(signal.SIGTSTP, signal_receive)   # ctrl-z
    signal.signal(signal.SIGUSR1, signal_receive)   # ctrl-c


@ratelimited(com_meta_Limiter.API_LIMIT['anidb'][0] / com_meta_Limiter.API_LIMIT['anidb'][1])
def anidb(thread_db, download_data):
    logging.debug("here i am in anidb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['chart_lyrics'][0] / com_meta_Limiter.API_LIMIT['chart_lyrics'][1])
def chart_lyrics(thread_db, download_data):
    logging.debug("here i am in chart_lyrics rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['comicvine'][0] / com_meta_Limiter.API_LIMIT['comicvine'][1])
def comicvine(thread_db, download_data):
    logging.debug("here i am in comicvine rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['giantbomb'][0] / com_meta_Limiter.API_LIMIT['giantbomb'][1])
def giantbomb(thread_db, download_data):
    logging.debug("here i am in giantbomb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['imdb'][0] / com_meta_Limiter.API_LIMIT['imdb'][1])
def imdb(thread_db, download_data):
    logging.debug("here i am in imdb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['imvdb'][0] / com_meta_Limiter.API_LIMIT['imvdb'][1])
def imvdb(thread_db, download_data):
    logging.debug("here i am in imvdb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        metadata_uuid = metadata_music_video.metadata_music_video_lookup()
        if metadata_uuid is None:
            thread_db.srv_db_download_update_provider('theaudiodb', download_data['mdq_id'])


@ratelimited(com_meta_Limiter.API_LIMIT['musicbrainz'][0] / com_meta_Limiter.API_LIMIT['musicbrainz'][1])
def musicbrainz(thread_db, download_data):
    logging.debug("here i am in musicbrainz rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['netflixroulette'][0] / com_meta_Limiter.API_LIMIT['netflixroulette'][1])
def netflixroulette(thread_db, download_data):
    logging.debug("here i am in netflixroulette rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['omdb'][0] / com_meta_Limiter.API_LIMIT['omdb'][1])
def omdb(thread_db, download_data):
    logging.debug("here i am in omdb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['pitchfork'][0] / com_meta_Limiter.API_LIMIT['pitchfork'][1])
def pitchfork(thread_db, download_data):
    logging.debug("here i am in pitchfork rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['rotten_tomatoes'][0] / com_meta_Limiter.API_LIMIT['rotten_tomatoes'][1])
def rotten_tomatoes(thread_db, download_data):
    logging.debug("here i am in rotten_tomatoes rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['televisiontunes'][0] / com_meta_Limiter.API_LIMIT['televisiontunes'][1])
def televisiontunes(thread_db, download_data):
    logging.debug("here i am in televisiontunes rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['theaudiodb'][0] / com_meta_Limiter.API_LIMIT['theaudiodb'][1])
def theaudiodb(thread_db, download_data):
    logging.debug("here i am in theaudiodb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['thegamesdb'][0] / com_meta_Limiter.API_LIMIT['thegamesdb'][1])
def thegamesdb(thread_db, download_data):
    logging.debug("here i am in thegamesdb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['thelogodb'][0] / com_meta_Limiter.API_LIMIT['thelogodb'][1])
def thelogodb(thread_db, download_data):
    logging.debug("here i am in thelogodb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['themoviedb'][0] / com_meta_Limiter.API_LIMIT['themoviedb'][1])
def themoviedb(thread_db, download_data):
    logging.debug("here i am in moviedb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        metadata_uuid = metadata_movie.movie_search_tmdb(thread_db, download_data['mdq_download_json']['Path'])
        if metadata_uuid is None:
            thread_db.srv_db_download_update_provider('omdb', download_data['mdq_id'])
        else:
            thread_db.srv_db_update_media_id(download_data['mdq_download_json']['Media'], metadata_uuid)
            # determine if the metadata is not downloaded
            if thread_db.srv_db_meta_guid_by_tmdb(download_data['mdq_download_json']['ProviderMetaID']) is None:
                download_data['mdq_download_json'].update({'Status': 'Fetch'})
                thread_db.srv_db_download_update(json.dumps(download_data['mdq_download_json']), download_data['mdq_id'])
            else:
                thread_db.srv_db_Download_Delete(download_data['mdq_id'])
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        if download_data['mdq_download_json']['ProviderMetaID'][0:2] != 'tt': # imdb id check
            tmdb_id = metadata_movie.movie_fetch_tmdb_imdb(download_data['mdq_download_json']['ProviderMetaID'])
            if tmdb_id is not None:
                download_data['mdq_download_json'].update({'ProviderMetaID': tmdb_id})
                thread_db.srv_db_download_update(json.dumps(download_data['mdq_download_json']), download_data['mdq_id'])
        else:
            metadata_movie.movie_fetch_save_tmdb(thread_db, download_data['mdq_download_json']['ProviderMetaID'])
            download_data['mdq_download_json'].update({'Status': 'FetchCastCrew'})
            thread_db.srv_db_download_update(json.dumps(download_data['mdq_download_json']), download_data['mdq_id'])
    elif download_data['mdq_download_json']['Status'] == "FetchCastCrew":
        metadata_movie.movie_fetch_save_tmdb_cast_crew(thread_db, download_data['mdq_download_json']['ProviderMetaID'])
        download_data['mdq_download_json'].update({'Status': 'FetchReview'})
        thread_db.srv_db_download_update(json.dumps(download_data['mdq_download_json']), download_data['mdq_id'])
    elif download_data['mdq_download_json']['Status'] == "FetchReview":
        metadata_movie.movie_fetch_save_tmdb_review(thread_db, download_data['mdq_download_json']['ProviderMetaID'])
        thread_db.srv_db_Download_Delete(download_data['mdq_id'])


@ratelimited(com_meta_Limiter.API_LIMIT['thesportsdb'][0] / com_meta_Limiter.API_LIMIT['thesportsdb'][1])
def thesportsdb(thread_db, download_data):
    logging.debug("here i am in thesportsdb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['thetvdb'][0] / com_meta_Limiter.API_LIMIT['thetvdb'][1])
def thetvdb(thread_db, download_data):
    logging.debug("here i am in thetvdb rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['tvmaze'][0] / com_meta_Limiter.API_LIMIT['tvmaze'][1])
def tvmaze(thread_db, download_data):
    logging.debug("here i am in tvmaze rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['tv_intros'][0] / com_meta_Limiter.API_LIMIT['tv_intros'][1])
def tv_intros(thread_db, download_data):
    logging.debug("here i am in tv_intros rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


@ratelimited(com_meta_Limiter.API_LIMIT['tvshowtime'][0] / com_meta_Limiter.API_LIMIT['tvshowtime'][1])
def tvshowtime(thread_db, download_data):
    logging.debug("here i am in tvshowtime rate %s", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    if download_data['mdq_download_json']['Status'] == "Search":
        pass
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        pass


def worker(content_providers):
    """
    Worker thread for limiter
    """
    logging.debug("name: %s", content_providers)
    thread_db = database_base.MKServerDatabase()
    thread_db.srv_db_open(Config.get('DB Connections', 'PostDBHost').strip(),\
        Config.get('DB Connections', 'PostDBPort').strip(),\
        Config.get('DB Connections', 'PostDBName').strip(),\
        Config.get('DB Connections', 'PostDBUser').strip(),\
        Config.get('DB Connections', 'PostDBPass').strip())
#    while True:
    for row_data in thread_db.srv_db_Download_Read_by_Provider(content_providers):
        logging.debug("row: %s", row_data)
        # mdq_id,mdq_download_json
        if content_providers == 'anidb':
            anidb(thread_db, row_data)
        elif content_providers == 'chart_lyrics':
            chart_lyrics(thread_db, row_data)
        elif content_providers == 'comicvine':
            comicvine(thread_db, row_data)
        elif content_providers == 'giantbomb':
            giantbomb(thread_db, row_data)
        elif content_providers == 'imdb':
            imdb(thread_db, row_data)
        elif content_providers == 'imvdb':
            imvdb(thread_db, row_data)
        elif content_providers == 'netflixroulette':
            netflixroulette(thread_db, row_data)
        elif content_providers == 'omdb':
            omdb(thread_db, row_data)
        elif content_providers == 'pitchfork':
            pitchfork(thread_db, row_data)
        elif content_providers == 'televisiontunes':
            televisiontunes(thread_db, row_data)
        elif content_providers == 'theaudiodb':
            theaudiodb(thread_db, row_data)
        elif content_providers == 'thegamesdb':
            thegamesdb(thread_db, row_data)
        elif content_providers == 'thelogodb':
            thelogodb(thread_db, row_data)
        elif content_providers == 'themoviedb':
            themoviedb(thread_db, row_data)
        elif content_providers == 'thesportsdb':
            thesportsdb(thread_db, row_data)
        elif content_providers == 'thetvdb':
            thetvdb(thread_db, row_data)
        elif content_providers == 'tv_intros':
            tv_intros(thread_db, row_data)
        elif content_providers == 'tvmaze':
            tvmaze(thread_db, row_data)
        elif content_providers == 'tvshowtime':
            tvshowtime(thread_db, row_data)
        elif content_providers == 'Z':
            metadata_uuid = metadata_identification.metadata_identification(thread_db,\
                class_text_dict[row_data['mdq_download_json']['ClassID']],\
                row_data['mdq_download_json']['Path'], row_data['mdq_download_json'],\
                row_data['mdq_id'])
            # update the media row with the json media id AND THE proper NAME!!!
            if metadata_uuid is not None:
                logging.debug("update: %s %s",\
                    row_data['mdq_download_json']['MediaID'], metadata_uuid)
                thread_db.srv_db_update_media_id(row_data['mdq_download_json']['MediaID'], metadata_uuid)
                thread_db.srv_db_Download_Delete(row_data['mdq_id'])
    time.sleep(1)
    thread_db.srv_db_commit()
    thread_db.srv_db_close()
    return


# table the class_text into a dict...will lessen the db calls
class_text_dict = {}
for class_data in db.srv_db_media_class_list(None, None):
    class_text_dict[class_data['mm_media_class_guid']] = class_data['mm_media_class_type']


# grab the rate limiting providers and populate threads
with futures.ThreadPoolExecutor(len(com_meta_Limiter.API_LIMIT.keys())) as executor:
    futures = [executor.submit(worker, n) for n in com_meta_Limiter.API_LIMIT.keys()]
    for future in futures:
        logging.debug(future.result())


# log stop
db.srv_db_activity_insert('MediaKraken_Metadata API Stop', None,\
     'System: Metadata API Stop', 'ServerMetadataAPIStop', None, None, 'System')


# commit
db.srv_db_commit()


# close the database
db.srv_db_close()
