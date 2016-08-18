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
import pytest
import database as database_base


class TestDatabaseMediaRemote(object):


    @classmethod
    def setup_class(self):
        self.db_connection = database_base.MKServerDatabase()
        self.db_connection.db_open('127.0.0.1', 5432, 'metamandb', 'metamanpg', 'metamanpg')


    @classmethod
    def teardown_class(self):
        self.db_connection.db_close()


    # insert media into database
    # def db_insert_remote_media(self, media_link_uuid, media_uuid, media_class_uuid, media_metadata_uuid, media_ffprobe_json):
#        self.db_connection.db_rollback()


    # read in all media unless guid specified
    # def db_read_remote_media(self, media_guid=None):
#        self.db_connection.db_rollback()


    def test_db_known_remote_media_count(self):
        """
        # count known media
        """
        self.db_connection.db_rollback()
        self.db_connection.db_known_remote_media_count()


    # processed via main_link........
    ## process new records from network sync event from linked server
    #def db_Media_Remote_New_Data(self, link_uuid, link_records):
#        self.db_connection.db_rollback()


    # new media for link
    # def db_media_remote_read_new(self, date_last_sync, sync_movie=None, sync_tv=None, sync_sports=None, sync_music=None, sync_music_video=None, sync_book=None):
#        self.db_connection.db_rollback()
