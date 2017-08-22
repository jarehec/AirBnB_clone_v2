#!/usr/bin/python3
from fabric.api import run
import datetime
"""generates a .tgz archive from the contents of the web_static folder
"""


def do_pack():
    date = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    run("mkdir -p versions")
    try:
        run("tar -cvzf versions/web_static_{}.tgz /data/web_static"
            .format(date))
        return ("versions/web_static_{}.tgz".format(date))
    except:
        return None
