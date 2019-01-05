#!/bin/bash
##sudo unlink /etc/nginx/sites-enabled/default
##sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web
sudo gunicorn -b 0.0.0.0:8080 hello:application &
##sudo gunicorn -c /home/box/web/etc/wsgi.example hello:application
cd /home/box/web/ask
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application &
##sudo gunicorn -c /home/box/web/etc/django.conf ask.wsgi:application

##sudo ln -sf /home/box/web/etc/wsgi.example /etc/gunicorn.d/test
##sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
##sudo /etc/init.d/gunicorn restart test 
##sudo /etc/init.d/mysql start
