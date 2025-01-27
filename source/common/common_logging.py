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

import logging  # pylint: disable=W0611
import time


# rank
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


def com_logging_start(log_name="./log/MediaKraken_Main"):
    """
    Fire up logging processing and file with timestamp
    """
    logging.basicConfig(filename=(log_name + '_' + time.strftime("%Y%m%d%H%M%S")
                                  + '.log'), format='%(asctime)s: %(levelname)s %(message)s',
                        level=logging.INFO)
