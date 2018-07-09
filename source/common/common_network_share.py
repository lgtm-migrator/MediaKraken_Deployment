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

import os
import subprocess
from shlex import split

from . import common_global


def com_net_share_mount(share_list):
    # mount the share/dirs
    for share in share_list:
        common_global.es_inst.com_elastic_index('info', {'Attempting mount': share[
            'mm_media_share_type'], 'server':
                                                             share['mm_media_share_server'],
                                                         'path': share['mm_media_share_path']})
        # check for and create mount point
        if os.path.isdir('./mnt/' + share['mm_media_share_guid']):
            pass
        else:
            proc_dir = subprocess.Popen(split('mkdir ./mnt/\"' + share['mm_media_share_guid'] + '\"'))
            proc_dir.wait()
        mount_command = []
        mount_command.append('mount')
        mount_command.append('-t')
        if share['mm_media_share_type'] == 'nfs':
            mount_command.append('nfs')
            if share['mm_media_share_user'] != 'guest':
                mount_command.append('-o')
                mount_command.append('uid=1000')  # gid=1000
            mount_command.append(share['mm_media_share_server']
                                 + ':/' + share['mm_media_share_path'])
            mount_command.append('./mnt/%s' % share['mm_media_share_guid'])
        else:
            # unc/smb
            #            mount -t cifs //<host>/<path> /<localpath> -o user=<user>,password=<user>
            mount_command.append('cifs')
            mount_command.append('//' + share['mm_media_share_server'] + '/'
                                 + share['mm_media_share_path'])
            mount_command.append('./mnt/' + share['mm_media_share_guid'])
            if share['mm_media_share_user'] != 'guest':
                mount_command.append('-o')
                mount_command.append('user=' + share['mm_media_share_user']
                                     + ',password=' + share['mm_media_share_password'])
        common_global.es_inst.com_elastic_index('info', {'mount': mount_command})
        proc_mnt = subprocess.Popen(split(mount_command))
        proc_mnt.wait()
