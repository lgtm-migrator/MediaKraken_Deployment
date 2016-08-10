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

import sys
import logging
import subprocess
sys.path.append("../../MediaKraken_Common/radio_crawler")


# create the cache file for import
def MK_Common_Network_Radio():
    proc = subprocess.Popen(['python', '../MediaKraken_Common/radio_crawler/crawler_google.py'], shell=False)
    logging.debug("Crawler Google PID: %s", proc.pid)
    proc.wait()

    proc = subprocess.Popen(['python', '../MediaKraken_Common/radio_crawler/clean_uris.py'], shell=False)
    logging.debug("Clean Uris PID: %s", proc.pid)
    proc.wait()

    proc = subprocess.Popen(['python', '../MediaKraken_Common/radio_crawler/init_cache.py'], shell=False)
    logging.debug("Init Cache PID: %s", proc.pid)
    proc.wait()

    proc = subprocess.Popen(['python', '../MediaKraken_Common/radio_crawler/fetch_xiph.py'], shell=False)
    logging.debug("Fetch Xiph PID: %s", proc.pid)
    proc.wait()

    proc = subprocess.Popen(['python', '../MediaKraken_Common/radio_crawler/fetch_tags.py'], shell=False)
    logging.debug("Fetch Tags PID: %s", proc.pid)
    proc.wait()

    proc = subprocess.Popen(['python', '../MediaKraken_Common/radio_crawler/fetch_cast.py'], shell=False)
    logging.debug("Fetch Cast PID: %s", proc.pid)
    proc.wait()

    proc = subprocess.Popen(['python', '../MediaKraken_Common/radio_crawler/fetch_tags.py'], shell=False)
    logging.debug("Fetch Tags PID: %s", proc.pid)
    proc.wait()

    proc = subprocess.Popen(['python', '../MediaKraken_Common/radio_crawler/dump_taglist.py'], shell=False)
    logging.debug("Dump Taglist PID: %s", proc.pid)
    proc.wait()
