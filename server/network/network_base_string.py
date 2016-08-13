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
import logging
from twisted.internet.protocol import Factory, Protocol
from twisted.protocols.basic import Int32StringReceiver
import json
import os
import signal
import sys
sys.path.append("../MediaKraken_Common")
sys.path.append("../MediaKraken_Common/lib")
import ip2country
from common import common_logging
from common import common_network
import subprocess
try:
    import cPickle as pickle
except:
    import pickle


class NetworkEvents(Int32StringReceiver):
    """
    Process the network events for the server
    """
    # init is called on every connection
    def __init__(self, users, db, genre_list):
        self.MAX_LENGTH = 32000000
        self.cpu_use_table = {}
        # server info
        self.db = db
        self.users = users
        self.user_host_name = None
        self.user_ip_addy = None
        self.user_user_name = None
        self.user_slave = False
        self.user_verified = 0
        self.server_ip = common_network.mk_network_get_default_ip()
        # pull in the ini file config
        import ConfigParser
        self.config = ConfigParser.ConfigParser()
        self.config.read("MediaKraken.ini")
        # grab settings
        self.server_port = self.config.get('MediaKrakenServer', 'ListenPort').strip()
        self.server_port_image = self.config.get('MediaKrakenServer', 'ImageWeb').strip()
        self.server_port_ffmpeg = self.config.get('MediaKrakenServer', 'FFMPEG').strip()


    def connectionMade(self):
        """
        Network connection made from client so ask for ident
        """
        logging.info('Got Connection')
        self.sendString('IDENT')


    def connectionLost(self, reason):
        """
        Network connection dropped so remove client
        """
        logging.info('Lost Connection')
        if self.users.has_key(self.user_user_name):
            del self.users[self.user_user_name]


    def stringReceived(self, data):
        """
        Message received from client
        """
        msg = None
        messageWords = data.split(' ')
        logging.debug('GOT Data: %s', data)
        logging.debug('Message: %s', messageWords[0])
        if messageWords[0] == "VALIDATE":
            # have to create the self.player data so network knows how to send data back
            self.user_host_name = messageWords[1]
            self.user_ip_addy = str(self.transport.getPeer()).split('\'')[1]
            self.user_user_name = messageWords[1]
            # lookup the country
            country_data = ip2country.IP2Country(verbose=1).lookup(self.user_ip_addy)
            self.user_country_code = country_data[0]
            self.user_country_name = country_data[1]
            self.users[messageWords[1]] = self
            logging.debug("user: %s %s", self.user_host_name, self.user_ip_addy)
            if self.user_user_name == 'link':
                pass
        elif messageWords[0] == "PING":  # Client_Network
            msg = "PONG"
        # user commands
        elif messageWords[0] == "LOGIN":
            pass
# actually processed in "main_link" program!!!!
#        elif messageWords[0] == "RECEIVENEWMEDIA":
#            self.db.srv_db_Media_Link_New_Data(pickle.loads(messagewords[1])
        elif messageWords[0] == "REQUESTNEWMEDIA":
            msg = "RECEIVENEWMEDIA " + pickle.dumps(self.db.srv_db_Media_Link_Read_New(pickle.loads(messagewords[1]), message_Words[2], message_Words[3], message_Words[4], message_Words[5], message_Words[6], message_Words[7]))
        elif messageWords[0] == "PlayUUID" or messageWords[0] == "demo":
            #media_path = self.db.srv_db_media_path_by_uuid('0000be97-09de-446e-b45e-e0d3b93c44e7')[0][0]
            media_path = self.db.srv_db_media_path_by_uuid(messageWords[1])[0]
            if media_path is not None:
                if True:
                    # launch and attach to local running ffserver
                    http_link = 'http://localhost:' + self.server_port_ffmpeg + '/stream.ffm'
                    self.proc_ffmpeg_stream = subprocess.Popen(['ffmpeg', '-i',\
                        media_path, http_link], shell=False)
                    http_link = 'http://' + common_network.mk_network_get_default_ip() + ':'\
                        + self.server_port_ffmpeg + '/stream.ffm'
                else:
                    # tell slave to fire up the media
                    http_link = None
            msg = 'VIDPLAY ' + http_link
        elif messageWords[0] == "FlagMismatchUUID":
            pass
        elif messageWords[0] == "MediaIDUpdateUUID":
            # media id, metadata id
            self.db.srv_db_update_media_id(messageWords[1], messageWords[2])
        # metadata commands
        elif messageWords[0] == "IMAGE":
            lookup_id = None
            uuid_found = False
            # messageWords[1] is returned to show client which one is being refreshed
            media_id = None
            if messageWords[3] == 'None': # random movie selection
                if messageWords[2] == "MOVIE":
                    try:
                        lookup_id, media_id = self.db.srv_db_media_random(messageWords[5])
                    except:
                        pass
            else:
                # fetch specific id
                try:
                    lookup_id = json.loads(self.db.srv_db_media_image_path(messageWords[3])[0])[messageWords[4]] # use this to grab file path
                except:
                    pass
            if lookup_id is not None:
                msg = "IMAGE " + pickle.dumps((messageWords[1], 'https://'\
                    + self.server_ip.strip() + ':' + self.server_port_image.strip() + '/'\
                    + lookup_id.replace('../images/', ''), media_id))
        # general data
        elif messageWords[0] == "GENRELIST":
            msg = "GENRELIST " + pickle.dumps(self.genre_list)
        # theater data
        elif messageWords[0] == "VIDEODETAIL":
            msg = "VIDEODETAIL " + pickle.dumps(self.db.srv_db_read_media_Metadata_Both(messageWords[1]))
        elif messageWords[0] == "VIDEOGENRELIST":
            msg = "VIDEOLIST " + pickle.dumps(self.db.srv_db_web_media_list(self.db.srv_db_media_uuid_by_class("Movie"), messageWords[0], messageWords[1]))
        elif messageWords[0] == "movie" or messageWords[0] == "recent_addition" or messageWords[0] == 'in_progress' or messageWords[0] == 'video':
            msg = "VIDEOLIST " + pickle.dumps(self.db.srv_db_web_media_list(self.db.srv_db_media_uuid_by_class("Movie"), messageWords[0]))
        # admin commands
        elif messageWords[0] == "ScanMedia":
            # popen expects a list
            self.proc_file_scan = subprocess.Popen(['python', './subprogram/subprogram_file_scan.py'], shell=False)
        elif messageWords[0] == "ScanMediaStop":
            os.killpg(self.proc_file_scan.pid, signal.SIGUSR1)
        elif messageWords[0] == "MatchMedia":
            # popen expects a list
            self.proc_media_match = subprocess.Popen(['python', './subprogram/subprogram_match_known_media.py'], shell=False)
        elif messageWords[0] == "MatchMediaStop":
            os.killpg(self.proc_media_match.pid, signal.SIGUSR1)
        elif messageWords[0] == "CreateChapterImage":
            # popen expects a list
            self.proc_chapter_create = subprocess.Popen(['python', './subprogram/subprogram_create_chapter_images.py'], shell=False)
        elif messageWords[0] == "CreateChapterImageStop":
            os.killpg(self.proc_chapter_create.pid, signal.SIGUSR1)
        elif messageWords[0] == "ScudLeeAnimeMatch":
            # popen expects a list
            self.proc_anime_match = subprocess.Popen(['python', './subprogram/subprogram_match_anime_id_scudlee.py'], shell=False)
        elif messageWords[0] == "ScudLeeAnimeMatchStop":
            os.killpg(self.proc_anime_match.pid, signal.SIGUSR1)
        elif messageWords[0] == "SubtitleMedia":
            # popen expects a list
            self.proc_subtitle_media_match = subprocess.Popen(['python', './subprogram/subprogram_subtitle_downloader.py'], shell=False)
        elif messageWords[0] == "SubtitleMediaStop":
            os.killpg(self.proc_subtitle_media_match.pid, signal.SIGUSR1)
        elif messageWords[0] == "CPUUSAGE":
            self.cpu_use_table[self.user_ip_addy] = messageWords[1]
        elif messageWords[0] == "SHUTDOWN":
            self.db.srv_db_Close()
            sys.exit(0)
        else:
            loggging.error("UNKNOWN TYPE: %s", messageWords[0])
            msg = "UNKNOWN_TYPE"
        if msg is not None:
            logging.debug("should be sending data")
            self.Send_Single_User(msg)


    def Send_Single_User(self, message):
        for user_host_name, protocol in self.users.iteritems():
            if protocol == self:
                logging.debug('send single: %s', message)
                protocol.sendString(message.encode("utf8"))
                break


    def Send_All_Users(self, message):
        for user_host_name, protocol in self.users.iteritems():
            if self.users[user_host_name].user_verified == 1:
                logging.debug('send all: %s', message)
                protocol.sendString(message.encode("utf8"))


    def Send_All_Slaves(self, message):
        for user_host_name, protocol in self.users.iteritems():
            if self.users[user_host_name].user_slave:
                logging.debug('send all slave: %s', message)
                protocol.sendString(message.encode("utf8"))
