"""
Just a tiny script to get some data from ldap if you are lazy to open ldap GUI...
"""

import ldap
import configparser
import re

config = configparser.ConfigParser()
config.read('.credentials/work.ini')

search_filter = '(&(objectClass=*)(cn=csacs*))'
attributes = ['cn']
should_contain = "something"

l = ldap.initialize(f"ldap://{config['ldap']['host']}")

l.simple_bind_s(config['ldap']['user'], config['ldap']['pass'])

root = l.search_s(config['ldap']['base_dn'],
                  'ldap.SCOPE_ONELEVEL', 'objectclass=*', [])
print(root)

#r = l.search_s(config['ldap']['base_dn'],              ldap.SCOPE_SUBTREE, search_filter, attributes)

"""
for e in r[0][1]['memberOf']:
    if re.findall(should_contain,str(e)):
        print(e)
"""
