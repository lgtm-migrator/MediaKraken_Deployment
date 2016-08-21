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
import sys
import os
import signal
from common import common_config_ini
from common import common_file
import locale
locale.setlocale(locale.LC_ALL, '')

# create the file for pid
pid_file = './pid/' + str(os.getpid())
common_file.com_file_save_data(pid_file, 'IGDB_Downloader', False, False, None)

def signal_receive(signum, frame):
    print('CHILD IGDB: Received USR1')
    # remove pid
    os.remove(pid_file)
    # cleanup db
    db_connection.db_rollback()
    db_connection.db_close()
    sys.stdout.flush()
    sys.exit(0)


if str.upper(sys.platform[0:3]) == 'WIN' or str.upper(sys.platform[0:3]) == 'CYG':
    signal.signal(signal.SIGBREAK, signal_receive)   # ctrl-c
else:
    signal.signal(signal.SIGTSTP, signal_receive)   # ctrl-z
    signal.signal(signal.SIGUSR1, signal_receive)   # ctrl-c


total_download_attempts = 0
# main code
def main(argv):
    global total_download_attempts
    # search the directory for filter files


# open the database
config_handle, option_config_json, db_connection = common_config_ini.com_config_read()


if __name__ == "__main__":
    print('IGDB game info download attempts: %s', total_download_attempts)
    # send notications
    if total_download_attempts > 0:
        db_connection.db_notification_insert(locale.format('%d',\
            total_download_attempts, True) + " IGDB game info downloaded.", True)
    # commit all changes
    db_connection.db_commit()
    # close DB
    db_connection.db_close()
    # remove pid
    os.remove(pid_file)
