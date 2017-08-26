#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static
apt update
apt install -y nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo 'Hello World!' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
loc="location /hbnb_static {\n\talias /data/web_static/current;\n}"
sed -i "38i $loc" /etc/nginx/sites-available/default
service nginx start
service nginx reload
