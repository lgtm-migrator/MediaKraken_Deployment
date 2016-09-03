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

from __future__ import absolute_import, division, print_function, unicode_literals
import logging # pylint: disable=W0611
from twisted.internet import ssl
from twisted.internet import reactor
#from twisted.internet import protocol
from twisted.internet.protocol import Factory
import sys
from network import network_base_string as network_base
from common import common_config_ini
from common import common_logging
from time import time
import time  # yes, use both otherwise some time code below breaks
import signal


def signal_receive(signum, frame): # pylint: disable=W0613
    """
    Handle signal interupt
    """
    print('CHILD Reactor String: Received USR1')
    # cleanup db
    self.db_connection.db_rollback()
    self.db_connection.db_close()
    sys.stdout.flush()
    sys.exit(0)


class MediaKrakenServerApp(Factory):
    def __init__(self):
        # start logging
        common_logging.com_logging_start('./log/MediaKraken_Subprogram_Reactor_String')
        # set other data
        self.server_start_time = time.mktime(time.gmtime())
        self.users = {} # maps user names to network instances
        # open the database
        config_handle, option_config_json, self.db_connection = common_config_ini.com_config_read()
        # preload some data from database
        self.genre_list = self.db_connection.db_meta_genre_list()
        logging.info("Ready for connections!")


    def buildProtocol(self, addr):
        return network_base.mediakraken_network_events(self.users, self.db_connection,\
            self.genre_list)


if __name__ == '__main__':
    if str.upper(sys.platform[0:3]) == 'WIN' or str.upper(sys.platform[0:3]) == 'CYG':
        signal.signal(signal.SIGBREAK, signal_receive)   # ctrl-c # pylint: disable=E1101
    else:
        signal.signal(signal.SIGTSTP, signal_receive)   # ctrl-z
        signal.signal(signal.SIGUSR1, signal_receive)   # ctrl-c
    config_handle, option_config_json, db_connection = common_config_ini.com_config_read()
    # setup for the ssl keys
    reactor.listenSSL(int(option_config_json['MediaKrakenServer']['ListenPort']),\
        MediaKrakenServerApp(),\
        ssl.DefaultOpenSSLContextFactory('key/privkey.pem', 'key/cacert.pem'))
    reactor.run()
