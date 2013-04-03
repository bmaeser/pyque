# -*- coding: utf-8 -*-

import os
from datetime import datetime

from pyque.utils import sh


def mysqldump(filename, dbname, username=None, password=None, host=None,
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
