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


import pytest
import sys
sys.path.append("../MediaKraken_Common")
from MK_Common_Network_Twitch import *


class Test_MK_Common_Twitch_API:


    @classmethod
    def setup_class(self):
        self.db = MK_Common_Network_Twitch.MK_Common_Twitch_API()


    @classmethod
    def teardown_class(self):
        pass


    @pytest.mark.parametrize(("stream_limit"), [
        (0),
        (5)])
    def test_MK_Common_Twitch_Get_All_Streams(self, stream_limit):
        self.db.MK_Common_Twitch_Get_All_Streams(stream_limit)


    def test_MK_Common_Twitch_Get_Featured_Streams(self):
        self.db.MK_Common_Twitch_Get_Featured_Streams()


    def test_MK_Common_Twitch_Get_Summary(self):
        self.db.MK_Common_Twitch_Get_Summary()


    def test_MK_Common_Twitch_Get_Summary_Viewers(self):
        self.db.MK_Common_Twitch_Get_Summary_Viewers()


#    def MK_Common_Twitch_Channel_By_User(self, user_name):


#    def MK_Common_Twitch_By_Name(self, user_name):


#    def MK_Common_Twitch_Channel_By_Name(self, channel_name):


#    def MK_Common_Twitch_Get_Videos_By_Channel(self, channel_name, stream_limit):


#    def MK_Common_Twitch_Channel_Teams_By_Name(self, channel_name):


#    def MK_Common_Twitch_Search_Channel_By_Name(self, channel_name):


#    def MK_Common_Twitch_Search_Streams_By_Name(self, stream_game):


#    def MK_Common_Twitch_Search_Games_By_Name(self, game_name):
