#!/bin/bash
##sudo unlink /etc/nginx/sites-enabled/default
##sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/wsgi.example /etc/gunicorn.d/test
##sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart test 
##sudo /etc/init.d/mysql start