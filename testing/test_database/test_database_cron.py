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
import database as database_base


class TestDatabaseCron(object):


    @classmethod
    def setup_class(self):
        self.db_connection = database_base.MKServerDatabase()
        self.db_connection.srv_db_open('127.0.0.1', 5432, 'metamandb', 'metamanpg', 'metamanpg')


    @classmethod
    def teardown_class(self):
        self.db_connection.srv_db_close()


    def test_srv_db_cron_list_count(self):
        """
        # return cron count
        """
        self.db_connection.srv_db_rollback()
        self.db_connection.srv_db_cron_list_count()


    def test_srv_db_cron_list_count_false(self):
        self.db_connection.srv_db_rollback()
        self.db_connection.srv_db_cron_list_count(False)


    def test_srv_db_cron_list_count_true(self):
        self.db_connection.srv_db_rollback()
        self.db_connection.srv_db_cron_list_count(True)


    @pytest.mark.parametrize(("enabled_only", "offset", "records"), [
        (False, None, None),
        (False, 100, 100),
        (False, 100000000, 1000),
        (True, None, None),
        (True, 100, 100),
        (True, 100000000, 1000)])
    def test_srv_db_cron_list(self, enabled_only, offset, records):
        """
        # return cron list
        """
        self.db_connection.srv_db_rollback()
        self.db_connection.srv_db_cron_list(enabled_only, offset, records)


    # update cron run date
    # def srv_db_cron_time_update(self, cron_type):
#        self.db_connection.srv_db_rollback()
