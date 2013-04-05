# -*- encoding: utf-8 -*-

import os
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT



def sh(cmd):
    """ Executes the given command.
    returns a 2-tuple with returncode (integer) and OUTPUT (string)
    """

    # we mimic subprocess.check_output from python 2.7
    # to stay compatible with python 2.5+

    process = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    output, unused_err = process.communicate()
    retcode = process.poll()

    return (retcode, output)


def gzip(filename):
    """ Gzip a file
    """

    infodict = {}
    anyerror = False

    infodict['starttime'] = datetime.now()

    try:
        infodict['original_filesize'] = os.path.getsize(filename)
    except OSError:
        infodict['original_filesize'] = 0
        anyerror = True

    ## run gzip
    retcode, output = sh('gzip %s' % filename)
    
    if retcode != 0: anyerror = True

    infodict['error'] = anyerror
    infodict['errortext'] = None if retcode == 0 else output

    new_filename = filename+'.gz'
    

    infodict['new_filename'] = new_filename
    infodict['endtime'] = datetime.now()

    try:
        infodict['new_filesize'] = os.path.getsize(new_filename)
    except OSError:
        infodict['new_filesize'] = 0
        anyerror = True

    return infodict

def rotate(filename, targetdir, versions=None, archive_dir=None):
    """ Rotates a file.

    """