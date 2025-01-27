"""
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
"""

import subprocess

from common import common_logging_elasticsearch_httpx


class TestSubprogramTVMazeUpdate:
    """
    Test tvmaze
    """

    def test_sub_tvmaze_update(self):
        """
        Test function
        """
        proc_info = subprocess.Popen(
            ['python3', './subprogram_metadata_tvmaze_updates.py'], shell=False)
        common_logging_elasticsearch_httpx.com_es_httpx_post(message_type='info', message_text={
            'stuff': "PID: %s" % proc_info.pid})
        proc_info.wait()
