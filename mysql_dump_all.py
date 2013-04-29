# -*- coding: utf-8 -*-

'''
Creates a gziped dump of every MySQL database on localhost
'''

from pyque.db.mysql import db_list, db_dump
from pyque.utils import gzip

username = 'backupuser'
password = 'test'

for db in db_list(username = username, password=password):
    dumpfilename = '/tmp/' + db + '.sql'
    db_dump(dumpfilename, dbname=db, username=username, password=password)
    gzip(dumpfilename)
