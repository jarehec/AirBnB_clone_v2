#!/usr/bin/python3
from fabric.api import local
import datetime
"""generates a .tgz archive from the contents of the web_static folder
"""


def do_pack():
    date = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    file = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(file))
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file))
        return ("{}".format(file))
    except:
        return None
