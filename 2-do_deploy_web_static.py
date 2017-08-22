#!/usr/bin/python3
from fabric.api import local, run, put, env
import datetime
"""distributes an archive to the web servers
"""


env.hosts = ['66.70.184.235', '34.229.113.91']


def do_deploy(archive_path):
    if archive_path is None:
        return False
    try:
        put("versions/{}".format(archive_path), "/tmp/{}".format(archive_path))
        run("tar -xzf {} -C /data/web_static/releases/{}"
            .format(archive_path, archive_path[:-4]))
        run("rm -f {}".format(archive_path))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current"
            .format(archive_path[:-4]))
    except:
        return False
    return True
