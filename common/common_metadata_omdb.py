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
import logging
import sys
import os
import omdb


class MK_Common_OMDb_API:
    def __init__(self):
        pass


    def MK_Common_OMDb_Get(self, media_title, media_year, media_fullplot, media_tomatoes):
        omdb.get(title=media_title, year=media_year, fullplot=media_fullplot, tomatoes=media_tomatoes)


    def MK_Common_OMDb_Search(self, media_title):
        omdb.search(media_title)


    def MK_Common_OMDb_Search_Movie(self, media_title):
        omdb.search_movie(media_title)


    def MK_Common_OMDb_Search_Episode(self, media_title):
        omdb.search_episode(media_title)


    def MK_Common_OMDb_Search_Series(self, media_title):
        omdb.search_series(media_title)


    def MK_Common_OMDb_IMDB(self, IMDBid):
        omdb.imdbid(IMDBid)


    def MK_Common_OMDb_Title(self, media_title):
        omdb.title(media_title)


    def MK_Common_OMDb_Default(self):
        omdb.set_default('tomatoes', True)


    def MK_Common_OMDb_Request(self, media_title, media_year, media_fullplot, media_tomatoes):
        omdb.request(media_title, media_year, media_fullplot, media_tomatoes)
