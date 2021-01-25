#!/bin/bash

cd /code
# setup app using the django tools
python3 manage.py migrate
# django-constance models
python3 manage.py migrate database

mkdir /code/geomapshark/static/
echo yes | python3 manage.py compilemessages -l fr -l de -l it -l en

echo yes | python3 manage.py collectstatic

exec $@
