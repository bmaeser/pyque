# -*- coding: utf-8 -*-

import os
from datetime import datetime

import MySQLdb

from pyque.utils import sh


def db_dump(filename, dbname, username=None, password=None, host=None,
    port=None, tempdir='/tmp', mysqldump_path='mysqldump'):
    """Perfoms a mysqldump backup.
    Create a database dump for the given database.
    """

    infodict = {}
    anyerror = False

    infodict['starttime'] = datetime.now()

    filepath = os.path.join(tempdir, filename)

    cmd = mysqldump_path
    cmd += ' --result-file=' + os.path.join(tempdir, filename)

    if username:
        cmd += ' --user=%s' % username
    if host:
        cmd += ' --host=%s' % host
    if port:
        cmd += ' --port=%s' % port
    if password:
        cmd += ' --password=%s' % password

    cmd += ' ' + dbname

    ## run mysqldump
    retcode, output = sh(cmd)

    if retcode != 0: anyerror = True

    infodict['cmd'] = cmd
    infodict['endtime'] = datetime.now()
    infodict['filepath'] = filepath

    try:
        infodict['filesize'] = os.path.getsize(filepath)
    except OSError:
        infodict['filesize'] = 0
        anyerror = True
        
    infodict['error'] = anyerror
    infodict['errortext'] = None if retcode == 0 else output

    return infodict

def _cursor(username=None, password=None, host=None, port=None):
    "returns a connected cursor to the database-server."

    c_opts = {}

    if username: c_opts['user'] = username
    if password: c_opts['passwd'] = password
    if host: c_opts['host'] = host
    if port: c_opts['port'] = port

    dbc = MySQLdb.connect(**c_opts)
    dbc.autocommit(True)
    cur = dbc.cursor()
    return cur

def db_list(username=None, password=None, host=None, port=None):
    "returns a list of all databases on this server"

    cur = _cursor(username=username, password=password, host=host, port=port)
    cur.execute('SHOW DATABASES')
    rows = cur.fetchall()

    result = []
    for row in rows:
        result.append(row[0])

    return result




