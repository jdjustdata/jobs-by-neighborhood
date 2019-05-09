#!/usr/bin/env bash

python manage.py makemessages -l es
python manage.py compilemessages
python manage.py makemigrations
python manage.py migrate
