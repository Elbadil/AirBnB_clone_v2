#!/usr/bin/python3
"""Defining a function do_pack"""
from fabric.api import local
from datetime import datetime as date


def do_pack():
    """returns the archive path"""
    # Getting the date of the archive file
    date_now = date.now().strftime('%Y%m%d%H%M%S')

    # Defining the archive file
    archive_file = "versions/web_static_{}.tgz".format(date_now)

    # Creating a directory versions if not exist
    local('mkdir -p versions')

    # Copying the files web_static to the archive files
    archive = local("tar -czvf {} web_static".format(archive_file))

    # Creturn the archive path if the archive has been correctly generated
    if archive.return_code == 0:
        return archive_file
    else:
        return None
