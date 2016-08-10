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

import ldap
import logging


class MK_Common_LDAP_API:
    def __init__(self, ldap_server, ou_name, dc_name):
        # Initialize connection
        try:
            self.con = ldap.initialize('ldap://%s', ldap_server)
        except ldap.LDAPError, e:
            print e.message['info']
            if type(e.message) == dict and e.message.has_key('desc'):
                print e.message['desc']
            else:
                print e
        # Bind to the server (ie. actually connect) - not needed as simple_bind for check
        #self.con.simple_bind("ou=People,dc=hotbot,dc=com")
        self.ou_name = ou_name
        self.dc_name = dc_name


    def MK_Common_LDAP_Logon(self, user_name, user_password):
        # ldap logon check
        try:
            dn = "sAMAccountName=" + user_name + ",dc=" + dc_name + ",dc=local"
            self.con.simple_bind_s(dn, user_password)
        except ldap.INVALID_CREDENTIALS, e:
            return "INVALID_LOGIN"
        except ldap.LDAPError, e:
            print e.message['info']
            if type(e.message) == dict and e.message.has_key('desc'):
                print e.message['desc']
            else:
                print e


    def MK_Common_LDAP_Close(self):
        # Close the connection
        self.con.unbind_s()
