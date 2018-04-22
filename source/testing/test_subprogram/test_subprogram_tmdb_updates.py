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
import subprocess
import logging
import pytest  # pylint: disable=W0611


class TestSubprogramTMDBUpdates(object):
    """
    Test tmdb update
    """

    def test_sub_tmdb_update(self):
        """
        Test function
        """
        proc_info = subprocess.Popen(
            ['python', './subprogram_tmdb_updates.py'], shell=False)
        common_global.es_inst.com_elastic_index('info', {'stuff':"PID: %s", proc_info.pid)
        proc_info.wait()