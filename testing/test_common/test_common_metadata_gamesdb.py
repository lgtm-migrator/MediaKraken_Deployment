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
sys.path.append("../common")
from com_Metadata_GamesDB import *


class TestCommonMetadataGamesDB(object):


    @classmethod
    def setup_class(self):
        self.db = com_Metadata_GamesDB.com_Metadata_GamesDB_API()


    @classmethod
    def teardown_class(self):
        pass


    def Test_com_Metadata_GamesDB_Platform_List(self):
        com_Metadata_GamesDB_Platform_List()


# def com_Metadata_GamesDB_Platform_By_ID(self, platform_id):


    # 'mega man' as mega OR man
    def Test_com_Metadata_GamesDB_Games_By_Name_Or(self):
        com_Metadata_GamesDB_Games_By_Name_Or("Mega Man")


    # 'mega man' as mega AND man
    def Test_com_Metadata_GamesDB_Games_By_Name_And(self):
        com_Metadata_GamesDB_Games_By_Name_And("Mega Man")


# def com_Metadata_GamesDB_Games_By_Name_And_Platform_Or(self, game_name, platform_name, game_genre=None):


# def com_Metadata_GamesDB_Games_By_Name_And_Platform_And(self, game_name, platform_name, game_genre=None):


# def com_Metadata_GamesDB_Games_By_Platform_ID(self, platform_id):


# def com_Metadata_GamesDB_Games_By_ID(self, game_id):
