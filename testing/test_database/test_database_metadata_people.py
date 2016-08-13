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
import pytest
import sys
sys.path.append("./common")
sys.path.append("./server") # for db import
import database as database_base


class TestDatabaseMetadataPeople(object):


    @classmethod
    def setup_class(self):
        self.db = database_base.MK_Server_Database()
        self.db.srv_db_Open('127.0.0.1', 5432, 'metamandb', 'metamanpg', 'metamanpg')


    @classmethod
    def teardown_class(self):
        self.db.srv_db_Close()


    # count person metadata
    def Test_srv_db_metadata_person_list_count(self):
        self.db.srv_db_metadata_person_list_count()
        self.db.srv_db_Rollback()


    # return list of people
    @pytest.mark.parametrize(("offset", "records"), [
        (None, None),
        (100, 100),
        (100000000, 1000)])
    def Test_srv_db_metadata_person_list(self, offset, records):
        self.db.srv_db_metadata_person_list(offset, records)
        self.db.srv_db_Rollback()


    # return person data
    # def srv_db_metadata_person_by_guid(self, guid):
#         self.db.srv_db_Rollback()


    # return person data by name
    # def srv_db_metadata_person_by_name(self, person_name):
#         self.db.srv_db_Rollback()


    # does person exist already by host/id
    # def srv_db_metadata_person_id_count(self, host_type, guid):
#         self.db.srv_db_Rollback()


    # insert person
    # def srv_db_metdata_person_insert(self, person_name, media_id_json, person_json, image_json=None):
#         self.db.srv_db_Rollback()


    # batch insert from json of crew/cast
    # def srv_db_metadata_person_insert_cast_crew(self, meta_type, person_json):
#         self.db.srv_db_Rollback()


    # find other media for person
    # def srv_db_metadata_person_as_seen_in(self, person_guid):
#         self.db.srv_db_Rollback()
