# -*- coding: utf-8 -*-

from datetime import datetime

from pyque.utils import sh

def pg_dump(dbname, username, password, host='localhost', port='5432',
        socket=None, tempdir='/tmp', pg_dump_path='pg_dump'):

    statusdict = {}
    
    statusdict['starttime'] = datetime.utcnow()

    retcode, output = sh('ls -la')

    statusdict['endtime'] = datetime.utcnow()
    statusdict['error'] = False if retcode == 0 else True
    statusdict['errortext'] = None if retcode == 0 else output

    #return statusdict
    return statusdict
