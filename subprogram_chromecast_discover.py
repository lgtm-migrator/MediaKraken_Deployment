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
import logging # pylint: disable=W0611
import ConfigParser
CONFIG_HANDLE = ConfigParser.ConfigParser()
CONFIG_HANDLE.read("MediaKraken.ini")
import sys
sys.path.append("./common")
from common import common_hardware_chromecast
from common import common_file
from common import common_logging
from common import common_string
import os
import json
import signal
import database as database_base
import locale
locale.setlocale(locale.LC_ALL, '')
#lock = threading.Lock()


# create the file for pid
pid_file = './pid/' + str(os.getpid())
common_file.com_file_save_data(pid_file, 'Chromecast_Scan', False, False, None)


def signal_receive(signum, frame):
    global global_end_program
    global_end_program = True
    print('CHILD Tuner Scan: Received USR1')
    # remove pid
    os.remove(pid_file)
    # cleanup db
    db.srv_db_rollback()
    db.srv_db_close()
    sys.stdout.flush()
    sys.exit(0)


# start logging
common_logging.com_logging_start('./log/MediaKraken_Subprogram_Chromecast_Discovery')


# open the database
db = database_base.MKServerDatabase()
db.srv_db_open(CONFIG_HANDLE.get('DB Connections', 'PostDBHost').strip(),\
    CONFIG_HANDLE.get('DB Connections', 'PostDBPort').strip(),\
    CONFIG_HANDLE.get('DB Connections', 'PostDBName').strip(),\
    CONFIG_HANDLE.get('DB Connections', 'PostDBUser').strip(),\
    CONFIG_HANDLE.get('DB Connections', 'PostDBPass').strip())


# log start
db.srv_db_activity_insert('MediaKraken_Server Chromecast Scan Start', None,\
    'System: Server Chromecast Scan Start', 'ServerChromecastScanStart', None, None, 'System')


# grab some dirs to scan and thread out the scans
if str.upper(sys.platform[0:3]) == 'WIN' or str.upper(sys.platform[0:3]) == 'CYG':
    signal.signal(signal.SIGBREAK, signal_receive)   # ctrl-c
else:
    signal.signal(signal.SIGTSTP, signal_receive)   # ctrl-z
    signal.signal(signal.SIGUSR1, signal_receive)   # ctrl-c


devices_added = 0


# look for devices
chrome = common_hardware_chromecast.CommonHardwareChromecast()
logging.debug("Chrome: %s", chrome)
for row_data in chrome.com_chromecast_discover_dict():
    logging.debug("Dict: %s", row_data)
    chrome.com_chromecast_connect_by_name(row_data)
    logging.debug("Connected!")
    cast_json = chrome.com_chromecast_info()
    logging.debug("Cast: %s", cast_json)
    print("status: %s", chrome.com_chromecast_status())
    db.srv_db_device_insert('cast', json.dumps({cast_json}))


if devices_added > 0:
    db.srv_db_notification_insert(locale.format('%d', devices_added, True)\
        + " Chromecast added.", True)


# log end
db.srv_db_activity_insert('MediaKraken_Server Chromecast Scan Stop', None,\
    'System: Server Chromecast Scan Stop', 'ServerChromecastScanStop', None, None, 'System')

# commit
db.srv_db_commit()

# close the database
db.srv_db_close()

# remove pid
os.remove(pid_file)
