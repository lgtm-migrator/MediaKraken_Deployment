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

import os
import subprocess

from build_image_directory import build_image_dirs
from build_trailer_directory import build_trailer_dirs
from common import common_global
from common import common_logging_elasticsearch
from common import common_metadata_limiter

# TODO should be using env variables
# build image directories if needed
if os.path.isdir('/mediakraken/web_app/MediaKraken/static/meta/images/backdrop/a'):
    pass
else:
    build_image_dirs()

# TODO should be using env variables
# build trailer directories if needed
if os.path.isdir('/mediakraken/web_app/MediaKraken/static/meta/trailers/trailer/a'):
    pass
else:
    build_trailer_dirs()

# start logging
common_global.es_inst = common_logging_elasticsearch.CommonElasticsearch('main_metadata_api')

# fire off wait for it script to allow rabbitmq connection
# doing here so I don't have to do it multiple times
wait_pid = subprocess.Popen(['/mediakraken/wait-for-it-ash.sh', '-h',
                             'mkrabbitmq', '-p', ' 5672'], shell=False)
wait_pid.wait()

# fire up the workers for each provider
for meta_provider in common_metadata_limiter.API_LIMIT.keys():
    common_global.es_inst.com_elastic_index('info', {'meta_provider': meta_provider})
    proc_api_fetch = subprocess.Popen(['python', './main_server_metadata_api_worker.py',
                                       meta_provider], shell=False)
proc_api_fetch.wait()  # so this doesn't end which will cause docker to restart
