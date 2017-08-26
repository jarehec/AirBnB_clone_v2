#!/usr/bin/python3
from fabric.api import local, run, put, env
import datetime
"""distributes an archive to the web servers
"""

env.hosts = ['66.70.184.235', '34.229.113.91']


def do_deploy(archive_path):
    if archive_path is None:
        return False
    ws_rs = "web_static/releases"
    ws = "web_static"
    try:
        filename = archive_path.split('/')[1]
        put("versions/{}".format(filename), "/tmp/{}".format(filename))
        run("mkdir -p /data/{}/{}".format(ws_rs, filename[:-4]))
        run("tar -xzf /tmp/{} -C /data/{}/{}/"
            .format(filename, ws_rs, filename[:-4]))
        run("rm /tmp/{}".format(filename))
        run("mv /data/{}/{}/{}/* /data/{}/{}"
            .format(ws_rs, filename[:-4], ws, ws_rs, filename[:-4]))
        run("rm -rf /data/{}/{}/{}".format(ws_rs, filename[:-4], ws))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/{}/{} /data/{}/current"
            .format(ws_rs, filename[:-4], ws))
    except Exception as e:
        print(e)
        return False
    return True
