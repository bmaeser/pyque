# -*- encoding: utf-8 -*-

import fnmatch
import re
import shutil
import os

from datetime import datetime


def rotate(filename, targetdir, max_versions=None, archive_dir=None):
    """ Rotates a file.
        moves original file.ext to targetdir/file-YYYY-MM-DD-THH:MM:SS.ext

        deletes all older files matching the same pattern in targetdir that 
        exceed the amount of max_versions.
        if versions = None, no old versions are deleted.

        if archive_dir is set, old versions are not deleted but moved to
        archive_dir

    """
    dtimeformat = '%Y-%m-%d-%H:%M:%S'

    now = datetime.now().strftime(dtimeformat)
    old_path, old_filename = os.path.split(filename)
    fileroot, ext = old_filename.split(os.extsep, 1)

    new_filename = fileroot + '-' + now + '.' + ext
    new_filepath = os.path.join(targetdir, new_filename)

    if max_versions:
        # find all files with same pattern that already exist in targetdir
        old_files = {}
        for file in os.listdir(targetdir):
            pattern = re.compile(
                '^%s-(?P<date>\d{4}-\d{2}-\d{2}-\d{2}:\d{2}:\d{2}).%s'
                % (fileroot, ext))
            if pattern.match(file):
                d = re.search(pattern, file).group('date')
                old_files[d] = file

        delkeys = old_files.keys()
        # sort delkeys by date, newest first
        delkeys.sort(key=lambda x: datetime.strptime(x, dtimeformat),
            reverse=True)
        
        # delete all keys, that should not be deleted
        del delkeys[0 : max_versions -1]
        
        # delete all not needed files
        for k in delkeys:
            fname = old_files[k]
            fpath = os.path.join(targetdir, fname)

            if archive_dir:
                shutil.move(fpath, os.path.join(archive_dir, fname))
            else:
                os.remove(fpath)


        shutil.move(filename, new_filepath)

        pass
    else:
        shutil.move(filename, new_filepath)

    return True
