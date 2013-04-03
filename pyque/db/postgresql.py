# -*- coding: utf-8 -*-

import os
from datetime import datetime

from pyque.utils import sh

def pg_dump(filename, dbname, username=None, password=None, host=None,
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

    """


    
    infodict = {}
    anyerror = False

    infodict['starttime'] = datetime.now()

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

