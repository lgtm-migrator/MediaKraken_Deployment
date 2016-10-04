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
from . import metadata_movie


def metadata_process(thread_db, provider_name, download_data):
    # TODO art, posters, trailers, etc in here as well
    if download_data['mdq_download_json']['Status'] == "Search":
        logging.debug('%s search', provider_name)
        metadata_search(thread_db, provider_name, download_data)
    elif download_data['mdq_download_json']['Status'] == "Fetch":
        logging.debug('%s fetch %s', provider_name,\
                      download_data['mdq_download_json']['ProviderMetaID'])
        metadata_fetch(thread_db, provider_name, download_data)
    elif download_data['mdq_download_json']['Status'] == "FetchCastCrew":
        logging.debug('%s fetchcastcrew', provider_name)
        metadata_castcrew(thread_db, provider_name, download_data)
    elif download_data['mdq_download_json']['Status'] == "FetchReview":
        logging.debug('%s fetchreview', provider_name)
        metadata_review(thread_db, provider_name, download_data)


def metadata_search(thread_db, provider_name, download_data):
    """
    Search for metadata via specified provider
    """
    if provider_name == 'themoviedb':
        metadata_uuid, match_result = metadata_movie.movie_search_tmdb(thread_db,\
            download_data['mdq_download_json']['Path'])
        logging.debug('metadata_uuid %s, match_result %s', metadata_uuid, match_result)
        # if match_result is an int, that means the lookup found a match but isn't in db
        if metadata_uuid is None and type(match_result) != int:
            thread_db.db_download_update_provider('omdb', download_data['mdq_id'])
        else:
            if metadata_uuid is None:
                # not in the db so mark fetch
                # first verify a download que record doesn't exist for this id
                metadata_uuid = thread_db.db_download_que_exists(download_data['mdq_id'],\
                    'themoviedb', str(match_result))
                logging.debug('metaquelook: %s', metadata_uuid)
                if metadata_uuid is not None:
                    thread_db.db_update_media_id(download_data['mdq_download_json']['MediaID'],\
                        metadata_uuid)
                    # found in database so remove from download que
                    thread_db.db_download_delete(download_data['mdq_id'])
                else:
                    thread_db.db_update_media_id(download_data['mdq_download_json']['MediaID'],\
                                                 metadata_uuid)
                    download_data['mdq_download_json'].update({'ProviderMetaID': str(match_result)})
                    download_data['mdq_download_json'].update({'Status': 'Fetch'})
                    thread_db.db_download_update(json.dumps(download_data['mdq_download_json']),\
                        download_data['mdq_id'])
            else:
                # update with found metadata uuid from db
                thread_db.db_update_media_id(download_data['mdq_download_json']['MediaID'],\
                    metadata_uuid)
                # found in database so remove from download que
                thread_db.db_download_delete(download_data['mdq_id'])


def metadata_fetch(thread_db, provider_name, download_data):
    """
    Fetch main metadata for specified provider
    """
    if provider_name == 'themoviedb':
        if download_data['mdq_download_json']['ProviderMetaID'][0:2] == 'tt': # imdb id check
            tmdb_id = metadata_movie.movie_fetch_tmdb_imdb(\
                download_data['mdq_download_json']['ProviderMetaID'])
            if tmdb_id is not None:
                download_data['mdq_download_json'].update({'ProviderMetaID': str(tmdb_id)})
                thread_db.db_download_update(json.dumps(download_data['mdq_download_json']),\
                    download_data['mdq_id'])
        else:
            metadata_movie.movie_fetch_save_tmdb(thread_db,\
                download_data['mdq_download_json']['ProviderMetaID'],\
                download_data['mdq_download_json']['MetaNewID'])
            download_data['mdq_download_json'].update({'Status': 'FetchCastCrew'})
            thread_db.db_download_update(json.dumps(download_data['mdq_download_json']),\
                download_data['mdq_id'])


def metadata_castcrew(thread_db, provider_name, download_data):
    """
    Fetch cast/crew from specified provider
    """
    if provider_name == 'themoviedb':
        metadata_movie.movie_fetch_save_tmdb_cast_crew(thread_db,\
            download_data['mdq_download_json']['ProviderMetaID'],\
            download_data['mdq_download_json']['MetaNewID'])
    # setup for FetchReview
    download_data['mdq_download_json'].update({'Status': 'FetchReview'})
    thread_db.db_download_update(json.dumps(download_data['mdq_download_json']),\
        download_data['mdq_id'])


def metadata_review(thread_db, provider_name, download_data):
    """
    Fetch reviews from specified provider
    """
    if provider_name == 'themoviedb':
        metadata_movie.movie_fetch_save_tmdb_review(thread_db,\
            download_data['mdq_download_json']['ProviderMetaID'])
    # review is last.....so can delete download que
    thread_db.db_download_delete(download_data['mdq_id'])
