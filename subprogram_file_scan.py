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
from datetime import datetime # to handle threading
import os
import uuid
from concurrent import futures
import time
import json
import locale
locale.setlocale(locale.LC_ALL, '')
from common import common_config_ini
from common import common_network_cifs
from common import common_ffmpeg
from common import common_file
from common import common_logging
from common import common_signal
from common import common_string
#lock = threading.Lock()


MEDIA_EXTENSION = [
    'webm',
    'mkv',
    'flv',
    'vob',
    'ogv',
    'ogg',
    'drc',
    'mng',
    'avi',
    'mov',
    'qt',
    'wmv',
    'wma',
    'yuv',
    'rm',
    'rmvb',
    'asf',
    'mp4',
    'm4p',
    'm4v',
    'mpg',
    'mp2',
    'mpeg',
    'mpe',
    'mp3',
    'flac',
    'mpv',
    'm2v',
    'm4v',
    'nsv',
    'iso',
    'chd',
    'zip',
    '7z',
    'pdf',
    'srt',
]


MEDIA_EXTENSION_SKIP_FFMPEG = [
    'pdf',
    'zip',
    '7z',
    'iso',
    'chd',
    'srt',
]


# set signal exit breaks
common_signal.com_signal_set_break()


# start logging
common_logging.com_logging_start('./log/MediaKraken_Subprogram_File_Scan')


# TODO move this into worker function......no reason for this to be seperate anymore
# perform media scan
def mk_server_media_scan_audit(thread_db, dir_path, media_class_type_uuid, known_media_file,\
        dir_guid, class_text_dict):
    total_files = 0
    logging.info("Scan dir: %s %s", dir_path, media_class_type_uuid)
    # update the timestamp now so any other media added DURING this scan don't get skipped
    thread_db.db_audit_dir_timestamp_update(dir_path)
    thread_db.db_audit_path_update_status(dir_guid,\
        json.dumps({'Status': 'File scan', 'Pct': 100}))
    thread_db.db_commit()
    # check for UNC before grabbing dir list
    if dir_path[:1] == "\\":
        file_data = []
        smb_stuff = common_network_cifs.CommonCIFSShare()
        addr, share, path = common_string.com_string_unc_to_addr_path(dir_path)
        smb_stuff.com_cifs_connect(addr)
        for dir_data in smb_stuff.com_cifs_walk(share, path):
            for file_name in dir_data[2]:
                file_data.append('\\\\' + addr + '\\' + share + '\\' + dir_data[0]\
                    + '\\' + file_name)
        smb_stuff.com_cifs_close()
    else:
        file_data = common_file.com_file_dir_list(dir_path, None, True, False)
    total_file_in_dir = len(file_data)
    total_scanned = 0
    for file_name in file_data:
        # TODO whined about converting both to utf8
        if file_name in known_media_file:
            pass # already scanned, skip
        else:
            fileName, fileExtension = os.path.splitext(file_name)
            if fileExtension[1:].lower() in MEDIA_EXTENSION:
                total_files += 1
                fileName, fileExtension = os.path.splitext(file_name)
                new_class_type_uuid = media_class_type_uuid
                # video game data, don't do ffmpeg
                if thread_db.db_media_class_by_uuid(media_class_type_uuid) == 'Video Game':
                    if fileExtension.lower() == 'iso':
                        new_class_type_uuid = class_text_dict['Game ISO']
                    elif fileExtension.lower() == 'chd':
                        new_class_type_uuid = class_text_dict['Game CHD']
                    else:
                        new_class_type_uuid = class_text_dict['Game ROM']
                    # TODO lookup game info in game database data
                    media_ffprobe_json = None
                # if an extention skip
                elif fileExtension.lower() in MEDIA_EXTENSION_SKIP_FFMPEG:
                    media_ffprobe_json = None
                else:
                    if file_name.find('/trailers/') != -1 or file_name.find('/theme.mp3') != -1\
                            or file_name.find('/theme.mp4') != -1\
                            or file_name.find('\\trailers\\') != -1\
                            or file_name.find('\\theme.mp3') != -1\
                            or file_name.find('\\theme.mp4') != -1:
                        media_class_text = thread_db.db_media_class_by_uuid(new_class_type_uuid)
                        if media_class_text == 'Movie':
                            if file_name.find('/trailers/') != -1\
                                    or file_name.find('\\trailers\\') != -1:
                                new_class_type_uuid = class_text_dict['Movie Trailer']
                            else:
                                new_class_type_uuid = class_text_dict['Movie Theme']
                        elif media_class_text == 'TV Show' or media_class_text == 'TV Episode'\
                                or media_class_text == 'TV Season':
                            if file_name.find('/trailers/') != -1\
                                    or file_name.find('\\trailers\\') != -1:
                                new_class_type_uuid = class_text_dict['TV Trailer']
                            else:
                                new_class_type_uuid = class_text_dict['TV Theme']
                    elif file_name.find('/extras/') != -1 or file_name.find('\\extras\\') != -1:
                        new_class_type_uuid = None
                    elif file_name.find('/backdrops/') != -1\
                            or file_name.find('\\backdrops\\') != -1:
                        media_class_text = thread_db.db_media_class_by_uuid(new_class_type_uuid)
                        if media_class_text == 'Movie':
                            if file_name.find('/theme.mp3') != -1\
                                    or file_name.find('/theme.mp4') != -1\
                                    or file_name.find('\\theme.mp3') != -1\
                                    or file_name.find('\\theme.mp4') != -1:
                                new_class_type_uuid = class_text_dict['Movie Theme']
                    # determine ffmpeg json data
                    if file_name[:1] == "\\":
                        file_name\
                            = file_name.replace('\\\\', 'smb://guest:\'\'@').replace('\\', '/')
                    media_ffprobe_json = common_ffmpeg.com_ffmpeg_media_attr(file_name)
                # create media_json data
                media_json = json.dumps({'DateAdded': datetime.now().strftime("%Y-%m-%d"),\
                    'ChapterScan': True})
                media_id = str(uuid.uuid4())
                thread_db.db_insert_media(media_id, file_name,\
                    new_class_type_uuid, None, media_ffprobe_json, media_json)
                # media id begin and download que insert
                thread_db.db_download_insert('Z', json.dumps({'MediaID': media_id,\
                    'Path': file_name, 'ClassID': new_class_type_uuid, 'Status': None,\
                    'MetaNewID': str(uuid.uuid4()), 'ProviderMetaID': None}))
        total_scanned += 1
        thread_db.db_audit_path_update_status(dir_guid,\
            json.dumps({'Status': 'File scan: ' + locale.format('%d', total_scanned, True)\
                + ' / ' + locale.format('%d', total_file_in_dir, True),\
                'Pct': (total_scanned / total_file_in_dir) * 100}))
        thread_db.db_commit()
    logging.info("Scan dir done: %s %s", dir_path, media_class_type_uuid)
    thread_db.db_audit_path_update_status(dir_guid, None) # set to none so it doens't show up
    thread_db.db_commit()
    return total_files


def worker(audit_directory):
    """
    Worker thread for each directory
    """
    data1, data2, dir_guid = audit_directory
    # open the database
    config_handle, option_config_json, thread_db = common_config_ini.com_config_read()
    logging.debug('value=%s', data1)
    total_files = mk_server_media_scan_audit(thread_db, data1, data2, global_known_media,\
        dir_guid, class_text_dict)
    if total_files > 0:
        thread_db.db_notification_insert(locale.format('%d', total_files, True)\
            + " file(s) added from " + data1, True)
    thread_db.db_commit()
    thread_db.db_close()
    return


# open the database
config_handle, option_config_json, db_connection = common_config_ini.com_config_read()


# log start
db_connection.db_activity_insert('MediaKraken_Server File Scan Start', None,\
    'System: Server File Scan Start', 'ServerFileScanStart', None, None, 'System')


# load in all media from DB
global_known_media = [] # pylint: disable=C0103
known_media = db_connection.db_known_media()
# verify rows were returned
if known_media is not None:
    for media_row in known_media:
        global_known_media.append(media_row['mm_media_path'].encode('utf-8'))
known_media = None


# table the class_text into a dict...will lessen the db calls
class_text_dict = {}
for class_data in db_connection.db_media_class_list(None, None):
    class_text_dict[class_data['mm_media_class_type']] = class_data['mm_media_class_guid']
logging.debug('class: %s', class_text_dict)


# determine directories to audit
audit_directories = [] # pylint: disable=C0103
for row_data in db_connection.db_audit_paths():
    logging.info("Audit Path: %s", row_data)
    # check for UNC
    if row_data['mm_media_dir_path'][:1] == "\\":
        smb_stuff = common_network_cifs.CommonCIFSShare()
        addr, share, path\
            = common_string.com_string_unc_to_addr_path(row_data['mm_media_dir_path'])
        smb_stuff.com_cifs_connect(addr)
        if smb_stuff.com_cifs_share_directory_check(share, path):
            if datetime.strptime(time.ctime(\
                    smb_stuff.com_cifs_share_file_dir_info(share, path).last_write_time),\
                    "%a %b %d %H:%M:%S %Y") > row_data['mm_media_dir_last_scanned']:
                audit_directories.append((row_data['mm_media_dir_path'],\
                    str(row_data['mm_media_class_guid']), row_data['mm_media_dir_guid']))
                db_connection.db_audit_path_update_status(row_data['mm_media_dir_guid'],\
                    json.dumps({'Status': 'Added to scan', 'Pct': 100}))
        else:
            db_connection.db_notification_insert('UNC Library path not found: %s'\
                % row_data['mm_media_dir_path'], True)
        smb_stuff.com_cifs_close()
    else:
        if not os.path.isdir(row_data['mm_media_dir_path']): # make sure the path still exists
            db_connection.db_notification_insert('Library path not found: %s'\
                % row_data['mm_media_dir_path'], True)
        else:
            # verify the directory inodes has changed
            if datetime.strptime(time.ctime(os.path.getmtime(row_data['mm_media_dir_path'])),\
                    "%a %b %d %H:%M:%S %Y") > row_data['mm_media_dir_last_scanned']:
                audit_directories.append((row_data['mm_media_dir_path'],\
                    str(row_data['mm_media_class_guid']), row_data['mm_media_dir_guid']))
                db_connection.db_audit_path_update_status(row_data['mm_media_dir_guid'],\
                    json.dumps({'Status': 'Added to scan', 'Pct': 100}))


# commit
db_connection.db_commit()


# start processing the directories
if len(audit_directories) > 0:
    # switched to this since tracebacks work this method
    with futures.ThreadPoolExecutor(len(audit_directories)) as executor:
        futures = [executor.submit(worker, n) for n in audit_directories]
        for future in futures:
            logging.debug(future.result())


# log end
db_connection.db_activity_insert('MediaKraken_Server File Scan Stop', None,\
    'System: Server File Scan Stop', 'ServerFileScanStop', None, None, 'System')


# commit
db_connection.db_commit()


# close the database
db_connection.db_close()
