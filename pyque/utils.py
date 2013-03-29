# -*- encoding: utf-8 -*-

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

