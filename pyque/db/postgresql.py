# -*- coding: utf-8 -*-

import os
from datetime import datetime

from pyque.utils import sh

def pg_dump(filename, dbname, username=None, password=None, host=None,
    port=None, tempdir='/tmp', pg_dump_path='pg_dump', format='p'):
    """Performs a pg_dump in 'custom' format (-Fc), which is suitable for
    pg_restore.

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

    
    statusdict = {}    
    statusdict['starttime'] = datetime.utcnow()

    filepath = os.path.join(tempdir, filename)

    command = pg_dump_path
    command += ' --format %s' % format
    command += ' --file ' + os.path.join(tempdir, filename)

    if username:
        command += ' --username %s' % username
    if host:
        command += ' --host %s' % host
    if port:
        command += ' --port %s' % port

    command += ' ' + dbname

    ## export pgpasswd
    if password:
        os.environ["PGPASSWORD"] = password

    retcode, output = sh(command)

    statusdict['cmd'] = command
    statusdict['endtime'] = datetime.utcnow()
    statusdict['filepath'] = filepath
    statusdict['filesize'] = os.path.getsize(filepath)
    statusdict['error'] = False if retcode == 0 else True
    statusdict['errortext'] = None if retcode == 0 else output

    #return statusdict
    return statusdict

