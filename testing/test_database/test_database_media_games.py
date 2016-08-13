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
import sys
sys.path.append("./common")
sys.path.append("./server") # for db import
import database as database_base


class TestDatabaseMediaGames(object):


    @classmethod
    def setup_class(self):
        self.db = database_base.MK_Server_Database()
        self.db.srv_db_Open('127.0.0.1', 5432, 'metamandb', 'metamanpg', 'metamanpg')


    @classmethod
    def teardown_class(self):
        self.db.srv_db_Close()


    # audited system list count
    def Test_com_media_game_system_list_count(self):
        self.db.com_media_game_system_list_count()
        self.db.srv_db_Rollback()


    # audited system list
    @pytest.mark.parametrize(("offset", "records"), [
        (None, None),
        (100,100),
        (100000000,1000)])
    def Test_com_media_game_system_list(self, offset, records):
        self.db.com_media_game_system_list(offset, records)
        self.db.srv_db_Rollback()


    # audited game list by system count
    # def com_media_game_list_by_system_count(self, system_id):
#        self.db.srv_db_Rollback()


    # audited game list by system
    # def com_media_game_list_by_system(self, system_id, offset=None, records=None):
#        self.db.srv_db_Rollback()


    # audited games list count
    def Test_com_media_game_list_count(self):
        self.db.com_media_game_list_count()
        self.db.srv_db_Rollback()


    # audited games list
    @pytest.mark.parametrize(("offset", "records"), [
        (None, None),
        (100,100),
        (100000000,1000)])
    def Test_com_media_game_list(self, offset, records):
        self.db.com_media_game_list(offset, records)
        self.db.srv_db_Rollback()
