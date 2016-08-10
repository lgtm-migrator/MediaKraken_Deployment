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
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MK_Watchdog_Handler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info("Modifed: %s", event.src_path)


    def on_deleted(self, event):
        # TODO then could remove the media (if a media file) from the db automatically
        logging.info("Deleted: %s", event.src_path)


    def on_moved(self, event):
        # TODO update media file path....if a media file
        logging.info("Moved: %s", event.src_path)


    def on_created(self, event):
        logging.info("Created: %s", event.src_path)


#    def on_any_event(self, event):
#        logging.info("Any!", event.src_path)
#        pass


# define watchdog class
class MK_Common_Watchdog_API:
    def MK_Common_Watchdog_Start(self, paths_to_watch):
        # start watchdog
        event_handler = MK_Watchdog_Handler()
        self.observer = Observer()
        # pull in all the audit dirs
        for row_data in paths_to_watch:
            logging.debug("path: %s", row_data[0])
            if os.path.isdir(row_data[0]) and not os.path.ismount(row_data[0]):
                self.observer.schedule(event_handler, path=row_data[0], recursive=False)
        self.observer.start()


# stop watchdog
    def MK_Common_Watchdog_Stop(self):
        self.observer.stop()
        self.observer.join()
