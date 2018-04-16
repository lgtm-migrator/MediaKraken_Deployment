'''
  Copyright (C) 2017 Quinn D Granfor <spootdev@gmail.com>

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

import giantbomb


class CommonMetadataGiantbomb(object):
    """
    Class for interfacing with Giantbomb
    """

    def __init__(self, api_key, user_agent):
        self.giantbomb_inst = giantbomb.Api(api_key, user_agent)

    def com_meta_gb_getplatforms(self, offset=0):
        return self.giantbomb_inst.getPlatforms(offset)


'''
search(str, offset)
getGame(game_id)
getGames(platform_id, offset)
getVideo(video_id)
getPlatform(platform_id)
getFranchise(franchise_id)
getFranchises(offset)
'''
