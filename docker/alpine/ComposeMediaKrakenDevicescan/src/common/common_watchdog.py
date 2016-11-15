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
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class CommonWatchdogHandler(FileSystemEventHandler):
    """
    Class for handling watchdog events
    """
    def on_modified(self, event):
        """
        File modified notification
        """
        logging.info("Modifed: %s", event.src_path)


    def on_deleted(self, event):
        """
        File deleted notification
        """
        # TODO then could remove the media (if a media file) from the db automatically
        logging.info("Deleted: %s", event.src_path)


    def on_moved(self, event):
        """
        File moved notification
        """
        # TODO update media file path....if a media file
        logging.info("Moved: %s", event.src_path)


    def on_created(self, event):
        """
        File created notification
        """
        logging.info("Created: %s", event.src_path)


#    def on_any_event(self, event):
#        logging.info("Any!", event.src_path)
#        pass


# define watchdog class
class CommonWatchdog(object):
    """
    Class for starting up watchdog
    """
    def __init__(self):
        self.observer = None


    def com_watchdog_start(self, paths_to_watch):
        """
        Start watchdog on specified list of paths(s)
        """
        event_handler = CommonWatchdogHandler()
        self.observer = Observer()
        # pull in all the audit dirs
        for row_data in paths_to_watch:
            logging.info("path: %s", row_data[0])
            if os.path.isdir(row_data[0]) and not os.path.ismount(row_data[0]):
                self.observer.schedule(event_handler, path=row_data[0], recursive=False)
        self.observer.start()


    def com_watchdog_stop(self):
        """
        Stop watchdog
        """
        self.observer.stop()
        self.observer.join()