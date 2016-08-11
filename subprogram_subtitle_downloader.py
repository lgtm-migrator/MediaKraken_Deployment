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
import sys
import os
import signal
sys.path.append("../common")
import MK_Common_File
import MK_Common_Logging

# create the file for pid
pid_file = '../pid/' + str(os.getpid())
MK_Common_File.MK_Common_File_Save_Data(pid_file, 'Sub_Subtitle_Down', False, False, None)

def signal_receive(signum, frame):
    print 'CHILD Subtitle: Received USR1'
    # remove pid
    os.remove(pid_file)
    # cleanup db
    db.MK_Server_Database_Rollback()
    db.MK_Server_Database_Close()
    sys.stdout.flush()
    sys.exit(0)

if str.upper(sys.platform[0:3]) == 'WIN' or str.upper(sys.platform[0:3]) == 'CYG':
    signal.signal(signal.SIGBREAK, signal_receive)   # ctrl-c
else:
    signal.signal(signal.SIGTSTP, signal_receive)   # ctrl-z
    signal.signal(signal.SIGUSR1, signal_receive)   # ctrl-c


# start logging
MK_Common_Logging.MK_Common_Logging_Start('./log/MediaKraken_Subprogram_Subtitle_Downloader')


total_download_attempts = 0
# main code
def main(argv):
    global total_download_attempts
    # parse arguments
    sub_lang = "en"
    # search the directory for filter files
    for media_row in MK_Common_File.MK_Common_File_Dir_List('/nfsmount/TV_Shows_Misc/', ('avi', 'mkv', 'mp4', 'm4v'), True):
        # run the subliminal fetch for episode
        logging.debug("title check: %s", media_row.rsplit('.', 1)[0] + "." + sub_lang + ".srt")
        # not os.path.exists(media_row.rsplit('.',1)[0] + ".en.srt") and not os.path.exists(media_row.rsplit('.',1)[0] + ".eng.srt")
        if not os.path.exists(media_row.rsplit('.', 1)[0] + "." + sub_lang + ".srt"):
            # change working dir so srt is saved in the right spot
            total_download_attempts += 1
            os.chdir(media_row.rsplit('/', 1)[0])
            f = os.popen(u"subliminal -l " + sub_lang + " -- \"" + media_row.encode("utf8") + "\"")
            cmd_output = f.read()
            loggin.debug("Download Status: %s", cmd_output)


if __name__ == "__main__":
    print 'Total subtitle download attempts:', total_download_attempts
    # remove pid
    os.remove(pid_file)
