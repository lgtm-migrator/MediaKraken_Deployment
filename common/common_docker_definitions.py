'''
  Copyright (C) 2018 Quinn D Granfor <spootdev@gmail.com>

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

DOCKER_ELK = ()

DOCKER_MUMBLE = ()

DOCKER_PORTAINER = (None,
                    'mkportainer',
                    'portainer/portainer',
                    True,
                    {"9000": 9000},
                    {'/var/run/docker.sock':
                         {'bind': '/var/run/docker.sock', 'mode': 'ro'},
                     '/var/opt/mediakraken/data':
                         {'bind': '/ data', 'mode': 'rw'}
                     },
                    True,
                    None
                    )

DOCKER_PGADMIN = ()

DOCKER_SMTP = ()
