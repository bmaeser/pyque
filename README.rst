======
pyque
======

pythonic devops toolbelt.

consider this beta.
its dogfed and somehow tested, but shipped without warranty

API MIGHT CHANGE UNTIL V 1.0 (yes i am serious)

------------
Installation
------------

with pip: ::
    
    $ pip install pyque

or: ::
    
    $ easy_install pyque

or checkout from github: ::

    $ git clone https://github.com/bmaeser/pyque.git
    $ cd pyque
    $ python setup.py install

-------
Example
-------

Create a gziped MySQL dump of every database on localhost for user 'backupuser'.
chmod backup to 400 and rotate it away and keep 7 versions of this backup: ::

    import os

    from pyque.db.mysql import db_list, db_dump
    from pyque.sh import gzip, chmod
    from pyque.utils import rotate

    username = 'backupuser'
    password = 'test'
    tmppath = '/tmp'
    backupdir = '/tmp/backups'

    for db in db_list(username = username, password=password):
        dumpfilename = os.path.join(tmppath,db) + '.sql'
        db_dump(dumpfilename, dbname=db, username=username, password=password)
        retcode, output, newfilepath = gzip(dumpfilename)
        chmod(newfilepath, '400')
        rotate(newfilepath, backupdir, max_versions=7)

----------
Contribute
----------

contributions welcome

pull-request please and/or create a issue on github

-------
LICENCE
-------

The MIT License (MIT)
Copyright © 2013 Bernhard Mäser, http://bmaeser.io

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
