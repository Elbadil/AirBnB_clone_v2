#!/usr/bin/python3
"""Defining a function do_deploy"""
from fabric.api import run, put, local, env
from datetime import datetime as date
import os


# Declaring my servers
env.hosts = ['54.89.182.156', '34.239.248.185']
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    # Declaring my servers
    env.hosts = ['378424-web-01', '378424-web-02']

    # In case the file at the path archive_path doesn't exist
    if not os.path.exists(archive_path):
        return False

    else:
        # Extracting the archive filename without extension
        archive_filename = archive_path.split('/')[-1]
        archive_name_no_extension = archive_filename.split('.')[0]

        # Uploading the archive to the tmp directory of the web server
        a_path = "/tmp/{}".format(archive_filename)
        put(local_path=archive_path, remote=a_path)

        # Defining the target folder for the archive file
        target_folder = "/data/web_static/releases/"

        # Defining the full path to the taget folder
        full_path = target_folder + archive_name_no_extension + "/"

        # Creating the full_path directory if not existed
        run("mkdir -p {}".format(full_path))

        # Using the tar command to extract the archive to the target folder
        run("tar -xzf {} -C {}".format(a_path, full_path))

        # Deleting the archive of from the web server
        run("rm {}".format(a_path))

        # Moving the contents of 'web_static' to the top-level directory
        run("mv -f {}/web_static/* {}".format(full_path, full_path))

        # Removing the now-empty 'web_static' subdirectory
        run("rm -rf {}/web_static".format(full_path))

        # Deleting the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Creating the symbolic link /data/web_static/current on the web server
        run("ln -s {} /data/web_static/current".format(full_path))

        return True
