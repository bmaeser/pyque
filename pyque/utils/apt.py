# -*- coding: utf-8 -*-

from fabric.api import *

def install(package):
    run('apt-get install %s' % package)

def remove(package):
    run('apt-get remove %s' % package)


def update(quiet=True):
    """
    Update package lists from all repositories.
    """
    option = '-qq' if quiet else '-q'
    run('apt-get update %s' % option)


def upgrade(quiet=True):
    """
    Upgrade all installed packages.
    """
    option = '-qq' if quiet else '-q'
    run('apt-get upgrade %s' % option)


def fullupgrade(quiet=True):
    """
    Update all packages from all repositories and install all avaliable updates.

    Shorthand for: ::
    
        update(quiet)
        upgrade(quiet)        
    """
    update()
    upgrade()

## todo:
# better quiet
# more options
# install and remove >1 packages