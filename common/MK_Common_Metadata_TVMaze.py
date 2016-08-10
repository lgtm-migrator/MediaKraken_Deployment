'''
  Copyright (C) 2015 Quinn D Granfor <spootdev@gmail.com>

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

import MK_Common_Network
import logging


# code to use
# http://www.tvmaze.com/api


class MK_Common_Metadata_TVMaze_API:
    def __init__(self):
        pass


    # show list 50 per page - 0 is first page
    def MK_Common_Metadata_TheMaze_Show_List(self, page_no=0):
        url_opts = page_no,
        return MK_Common_Network.MK_Network_Fetch_From_URL(('http://api.tvmaze.com/shows?page=%s' % url_opts), None)


    # show when last updated
    def MK_Common_Metadata_TheMaze_Show_Updated(self):
        # returns id's and timestamps of last changed
        return MK_Common_Network.MK_Network_Fetch_From_URL('http://api.tvmaze.com/updates/shows', None)


    # lookup show
    def MK_Common_Metadata_TheMaze_WideSearch(self, show_name, show_year=None):
        url_opts = show_name,
        return MK_Common_Network.MK_Network_Fetch_From_URL(('http://api.tvmaze.com/search/shows?q=%s' % url_opts), None)


    # lookup specific show
    def MK_Common_Metadata_TheMaze_NarrowSearch(self, show_name, show_year=None):
        url_opts = show_name,
        return MK_Common_Network.MK_Network_Fetch_From_URL(('http://api.tvmaze.com/singlesearch/shows?q=%s' % url_opts), None)


    # lookup specific id
    def MK_Common_Metadata_TheMaze_Show_By_ID(self, tvmaze_id, tvrage_id, imdb_id, tvdb_id, embed_info=True):
        result_json = None
        # tvmaze lookup and fetch embed info if needed
        if tvmaze_id is not None:
            url_opts = tvmaze_id,
            if embed_info:
                result_json = MK_Common_Network.MK_Network_Fetch_From_URL(('http://api.tvmaze.com/shows/%s?embed[]=episodes&embed[]=cast' % url_opts), None)
            else:
                result_json = MK_Common_Network.MK_Network_Fetch_From_URL(('http://api.tvmaze.com/shows/%s' % url_opts), None)
        else:
            # currently embed options don't work on the lookup calls
            if tvrage_id is not None and result_json is None:
                url_opts = tvrage_id,
                result_json = MK_Common_Network.MK_Network_Fetch_From_URL(('http://api.tvmaze.com/lookup/shows?tvrage=%s' % url_opts), None)
            elif imdb_id is not None and result_json is None:
                url_opts = imdb_id,
                result_json = MK_Common_Network.MK_Network_Fetch_From_URL(('http://api.tvmaze.com/lookup/shows?imdb=%s' % url_opts), None)
            elif tvdb_id is not None and result_json is None:
                url_opts = tvdb_id,
                result_json = MK_Common_Network.MK_Network_Fetch_From_URL(('http://api.tvmaze.com/lookup/shows?thetvdb=%s' % url_opts), None)
            if embed_info and result_json is not None:
                result_json = MK_Common_Metadata_TheMaze_Show_By_ID(self, result_json['id'], None, None, None, True)
        return result_json


    # people search (doesnt' appear to have episode data here)
    def MK_Common_Metadata_TheMaze_Person_By_Name(self, person_name):
        url_opts = person_name,
        return MK_Common_Network.MK_Network_Fetch_From_URL('http://api.tvmaze.com/search/people?q=%s' % url_opts)


    # schedule
    def MK_Common_Metadata_TheMaze_Schedule(self, country_code=None, schedule_date=None):
        result_json = MK_Common_Network.MK_Network_Fetch_From_URL('http://api.tvmaze.com/schedule', None)
        result_json = MK_Common_Network.MK_Network_Fetch_From_URL('http://api.tvmaze.com/schedule?country=US&date=2014-12-01', None)
        result_json = MK_Common_Network.MK_Network_Fetch_From_URL('http://api.tvmaze.com/schedule/full', None)
        return result_json
