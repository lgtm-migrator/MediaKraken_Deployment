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

import time

from common import common_global
from common import common_logging_elasticsearch
from common import common_signal
from network import network_base_line_ripper as network_base
from twisted.internet import reactor, protocol


class MediaKrakenServerApp(protocol.ServerFactory):
    def __init__(self):
        # start logging
        common_global.es_inst = common_logging_elasticsearch.CommonElasticsearch(
            'main_ripper_reactor_line')
        # set other data
        self.server_start_time = time.mktime(time.gmtime())
        self.users = {}  # maps user names to network instances
        common_global.es_inst.com_elastic_index('info', {'Ready for connections!': False})

    def buildProtocol(self, addr):
        return network_base.NetworkEvents(self.users, self.db_connection)


if __name__ == '__main__':
    # set signal exit breaks
    common_signal.com_signal_set_break()
    # setup for the ssl keys
    reactor.listenTCP(7000, MediaKrakenServerApp())
    reactor.run()