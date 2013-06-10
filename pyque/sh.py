# -*- encoding: utf-8 -*-

import os
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT

def quote(s):
    """ Return a shell escaped version of a string
    """
    return '%s' % (s.replace('\\', '\\\\')
        .replace('"', '\"')
        .replace('$', '\$')
        .replace('`', '\`')
        )


def sh(cmd, escape=True):
    """ Executes the given command.
    returns a 2-tuple with returncode (integer) and OUTPUT (string)
    """

    if escape:
        cmd = quote(cmd)

    process = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    output, unused_err = process.communicate()
    retcode = process.poll()

    return (retcode, output)


def gzip(filename):
    """ Gzip a file
    returns a 3-tuple with returncode (integer), terminal output (string)
    and the new filename.
    """

    ## run gzip
    retcode, output = sh('gzip %s' % filename)
    new_filename = filename+'.gz'

    return (retcode, output, new_filename)

def tar(filename, dirs=[], gzip=False):
    """ Create a tar-file or a tar.gz at location: filename.
    params:
        gzip: if True - gzip the file, default = False
        dirs: dirs to be tared
    returns a 3-tuple with returncode (integer), terminal output (string)
    and the new filename.
    """
    if gzip:
        cmd = 'tar czvf %s ' % filename
    else:
        cmd = 'tar cvf %s ' % filename

    if type(dirs) != 'list':
        dirs = [dirs]

    cmd += ' '.join(str(x) for x in dirs)

    retcode, output = sh(cmd)

    return (retcode, output, filename)

def chown(path, uid, guid, recursive=True):
    """ alternative to os.chown.
        wraps around unix chown
        example:
            chown('/tmp/test/', bob, bob)

        returns 2-tuple: exitcode and terminal output
    """

    if recursive:
        cmd = 'chown -R %s:%s %s' % (uid, guid, path)
    else:
        cmd = 'chown %s:%s %s' % (uid, guid, path)

    return sh(cmd)

def chmod(path, mode, recursive=True):
    """ alternative to os.
    """

    if recursive:
        cmd = 'chmod -R %s %s' % (mode, path)
    else:
        cmd = 'chmod %s %s' % (mode, path)

    return sh(cmd)

