# based on code from
# http://rendykstan.github.io/blog/2013/04/04/postgresql-vacuum-and-analyze-maintenance-and-performance/

from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import ConfigParser
config_handle = ConfigParser.ConfigParser()
config_handle.read("MediaKraken.ini")
import sys
sys.path.append("./server")
sys.path.append("./common")
import MK_Commong_Logging
import database as database_base


# start logging
common_logging.com_logging_start('./log/MediaKraken_Subprogram_Postgresql_Vacuum')


# open the database
db = database_base.MKServerDatabase()
db.srv_db_open(config_handle.get('DB Connections', 'PostDBHost').strip(),\
    config_handle.get('DB Connections', 'PostDBPort').strip(),\
    config_handle.get('DB Connections', 'PostDBName').strip(),\
    config_handle.get('DB Connections', 'PostDBUser').strip(),\
    config_handle.get('DB Connections', 'PostDBPass').strip())


# log start
db.srv_db_activity_insert('MediaKraken_Server Postgresql Vacuum Start', None,\
    'System: Server DB Vacuum Start', 'ServerVacuumStart', None, None, 'System')


# vacuum all the tables
# TODO this needed since open is autocommit?   db.srv_db_Postgesql_Set_Isolation_Level(0)
for row in db.srv_db_postgresql_vacuum_stat_by_day(1):
    logging.debug(row)
    db.srv_db_postgresql_vacuum_table(row['relname'])


# log end
db.srv_db_activity_insert('MediaKraken_Server Postgresql Vacuum Stop', None,\
    'System: Server DB Vacuum Stop', 'ServerVacuumStop', None, None, 'System')


# commit records
db.srv_db_commit()


# close the database
db.srv_db_close()
