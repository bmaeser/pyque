# -*- coding: utf-8 -*-

import os
from datetime import datetime

import psycopg2
import psycopg2.extras

from pyque.sh import sh

def dump(filename, dbname, username=None, password=None, host=None,
    port=None, tempdir='/tmp', pg_dump_path='pg_dump', format='p'):
    """Performs a pg_dump backup.

    It runs with the current systemuser's privileges, unless you specify
    username and password.

    By default pg_dump connects to the value given in the PGHOST environment
    variable.
    You can either specify "hostname" and "port" or a socket path.

    pg_dump expects the pg_dump-utility to be on $PATCH.
    Should that not be case you are allowed to specify a custom location with
    "pg_dump_path"

    Format is p (plain / default), c = custom, d = directory, t=tar

    returns statuscode and shelloutput

    """

    filepath = os.path.join(tempdir, filename)

    cmd = pg_dump_path
    cmd += ' --format %s' % format
    cmd += ' --file ' + os.path.join(tempdir, filename)

    if username:
        cmd += ' --username %s' % username
    if host:
        cmd += ' --host %s' % host
    if port:
        cmd += ' --port %s' % port

    cmd += ' ' + dbname

    ## export pgpasswd
    if password:
        os.environ["PGPASSWORD"] = password

    ## run pgdump
    return sh(cmd)


def _connection(username=None, password=None, host=None, port=None, db=None):
    "returns a connected cursor to the database-server."

    c_opts = {}

    if username: c_opts['user'] = username
    if password: c_opts['password'] = password
    if host: c_opts['host'] = host
    if port: c_opts['port'] = port
    if db: c_opts['database'] = db

    dbc = psycopg2.connect(**c_opts)
    dbc.autocommit = True
    return dbc

def db_list(username=None, password=None, host=None, port=None,
        maintain_db='postgres'):
    "returns a list of all databases on this server"

    conn = _connection(username=username, password=password, host=host,
        port=port, db=maintain_db)

    cur = conn.cursor()

    cur.execute('SELECT DATNAME from pg_database')
    rows = cur.fetchall()

    conn.close()

    result = []
    for row in rows:
        result.append(row[0])

    return result
