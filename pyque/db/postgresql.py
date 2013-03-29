# -*- coding: utf-8 -*-

import os
from datetime import datetime

from pyque.utils import sh

def pg_dump(filename, dbname, username=None, password=None, host=None,
    port=None, socket=None, tempdir='/tmp', pg_dump_path='pg_dump'):
    """Performs a pg_dump in 'custom' format (-Fc), which is suitable for
    pg_restore.

    It runs with the current systemuser's privileges, unless you specify
    username and password.

    By default pg_dump connects to the value given in the PGHOST environment
    variable.
    You can either specify "hostname" and "port", or give a unix-socket in
    "socket".

    pg_dump expects the pg_dump-utility to be on $PATCH.
    Should that not be case you are allowed to specify a custom location with
    "pg_dump_path"

    """

    
    statusdict = {}    
    statusdict['starttime'] = datetime.utcnow()

    filepath = os.path.join(tempdir, filename)

    command = 

    print command
    ## backup happens here
    retcode, output = sh('ls -la')


    statusdict['endtime'] = datetime.utcnow()
    statusdict['filepath'] = filepath
    statusdict['filesize'] = os.path.getsize(filepath)
    statusdict['error'] = False if retcode == 0 else True
    statusdict['errortext'] = None if retcode == 0 else output

    #return statusdict
    return statusdict
