# -*- encoding: utf-8 -*-

import fnmatch
import re
import shutil
import os

from datetime import datetime


def rotate(filename, targetdir, max_versions=None, archive_dir=None):
    """ Rotates a file.
        moves original file.ext to targetdir/YYYY-MM-DD-THH:MM:SS-file.ext

        deletes all older files matching the same pattern in targetdir that 
        exceed the amount of max_versions.
        if versions = None, no old versions are deleted.

        if archive_dir is set, old versions are not deleted but moved to
        archive_dir

    """
    now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    old_path, old_filename = os.path.split(filename)

    new_filename = now +'-'+ old_filename
    new_filepath = os.path.join(targetdir, new_filename)

    if max_versions:
        old_files = []
        for file in os.listdir(targetdir):
            pattern = re.compile('^\d{4}-\d{2}-\d{2}-\d{2}:\d{2}:\d{2}-%s'
                % old_filename)
            if pattern.match(file):
                old_files.append(file)

        old_files.sort() ## WIP HERE!

        print old_files
        # get list of existing files
        shutil.move(filename, new_filepath)
        # move file

        # delete or archive old ones
        pass
    else:
        shutil.move(filename, new_filepath)

    # print old_path
    # print old_filename
    # print new_filename

    return True