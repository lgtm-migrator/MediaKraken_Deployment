"""
  Copyright (C) 2021 Quinn D Granfor <spootdev@gmail.com>

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
import asyncio
import os
import shlex
import shutil
import subprocess
import sys

from common import common_file
from common import common_system

'''
# Mister file locations
/media/fat          	Micro SD card
/media/fat/_Arcade  	Upload Arcade cores here
/media/fat/_Computer	Upload Computer cores here
/media/fat/_Console 	Upload Console cores here
/media/fat/config   	Per core configs. Generated by each core as you use them
/media/fat/games    	Upload games/ROMs/images here
/media/fat/MiSTer.ini	MiSTer global config e.g. to change video mode / overscan
'''

source_directory = 'Y:\\Media\\Emulation'
target_directory = 'Y:\\Media\\Emulation\\misterfpga_share\\games'

# Mister folder name, source target dir, file extensions
file_conversion = (
    # CCC, ROM
    {'Target': 'CoCo2', 'Source': 'MAME 0.228 Software List ROMs (merged)\\coco_cart',
     'Conv': 'zip', 'Ext': 'rom', 'Enabled': False},

    # CUE, zip is a no no
    {'Target': 'MegaCD\megacd', 'Source': 'MAME 0.228 Software List CHDs (merged)\\megacd',
     'Conv': 'chd', 'Ext': 'dir', 'Enabled': True},

    # CUE, zip is a no no
    {'Target': 'MegaCD\megacdj', 'Source': 'MAME 0.228 Software List CHDs (merged)\\megacdj',
     'Conv': 'chd', 'Ext': 'dir', 'Enabled': True},

    # CUE, zip is a no no
    {'Target': 'MegaCD\segacd', 'Source': 'MAME 0.228 Software List CHDs (merged)\\segacd',
     'Conv': 'chd', 'Ext': 'dir', 'Enabled': False},

    # PCE, CUE
    {'Target': 'TGFX16-CD', 'Source': 'MAME 0.228 Software List CHDs (merged)\\pcecd',
     'Conv': 'chd', 'Ext': 'dir', 'Enabled': False},
)


async def main(loop):
    # start logging
    # await common_logging_elasticsearch_httpx.com_es_httpx_post_async(message_type='info',
    #                                                                  message_text='START',
    #                                                                  index_name='async_mister_converter')

    for mister_directory in file_conversion:
        if mister_directory['Enabled']:
            print('mister_directory:', mister_directory, flush=True)
            for file_data in common_file.com_file_dir_list(os.path.join(source_directory,
                                                                        mister_directory['Source']),
                                                           filter_text=mister_directory['Conv'],
                                                           walk_dir=True, skip_junk=False,
                                                           file_size=False, directory_only=False,
                                                           file_modified=False):
                print('file_data', file_data, flush=True)
                if os.path.splitext(file_data)[1][1:] == 'zip':
                    print('unzip:', mister_directory['Ext'], flush=True)
                    common_file.com_file_unzip(file_data,
                                               target_destination_directory=os.path.join(
                                                   source_directory,
                                                   mister_directory['Source']),
                                               remove_zip=False)
                    # walk dir to grab stuff that was in a folder
                    for unziped_file in common_file.com_file_dir_list(os.path.join(source_directory,
                                                                                   mister_directory[
                                                                                       'Source']),
                                                                      filter_text=mister_directory[
                                                                          'Ext'],
                                                                      walk_dir=True,
                                                                      skip_junk=False,
                                                                      file_size=False,
                                                                      directory_only=False,
                                                                      file_modified=False):
                        shutil.move(unziped_file,
                                    os.path.join(target_directory, mister_directory['Target']))
                elif os.path.splitext(file_data)[1][1:] == 'chd':
                    print('chd:', mister_directory['Ext'], flush=True)
                    # create dir to hold the cue/bin
                    print('target:', target_directory)
                    print('mistarget:', mister_directory['Target'])
                    print('split:', os.path.basename(os.path.splitext(file_data)[0]))
                    temp_dir = os.path.join(target_directory,
                                            mister_directory['Target'],
                                            os.path.basename(os.path.splitext(file_data)[0]))
                    print('temp dir:', temp_dir)
                    os.makedirs(temp_dir, exist_ok=True)
                    chd_pid = subprocess.Popen(
                        shlex.split('chdman extractcd -i "%s"'
                                    ' -o "%s.cue"'
                                    ' -ob "%s.bin"' %
                                    (file_data,
                                     os.path.join(temp_dir,
                                                  os.path.basename(os.path.splitext(file_data)[0])),
                                     os.path.join(temp_dir,
                                                  os.path.basename(
                                                      os.path.splitext(file_data)[0])))),
                        stdout=subprocess.PIPE, shell=False)
                    chd_pid.wait()
                    # # need to zip up the cue/bin and remove source
                    # common_file.com_file_zip(os.path.splitext(file_data)[0] + '.'
                    #                          + mister_directory['Ext'],
                    #                          (os.path.splitext(file_data)[0] + '.cue',
                    #                           os.path.splitext(file_data)[0] + '.bin'),
                    #                          remove_source_files=True)
                    # shutil.move(os.path.splitext(file_data)[0] + '.' + mister_directory['Ext'],
                    #             os.path.join(target_directory, mister_directory['Target']))

    # await common_logging_elasticsearch_httpx.com_es_httpx_post_async(message_type='info',
    #                                                                  message_text='STOP')


if __name__ == "__main__":
    # verify this program isn't already running!
    if common_system.com_process_list(
            process_name='/usr/bin/python3 /mediakraken/async_mister_converter.py'):
        sys.exit(0)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
