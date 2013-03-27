# -*- coding: utf-8 -*-
from fabric.api import *


def mysqldump(filename, dbname, user, password, port=5432,
    tempdir='/tmp', mysqldump_path='mysqldump'):
    """
    Create a database dump for the given database.


    """
    return "asdf"
