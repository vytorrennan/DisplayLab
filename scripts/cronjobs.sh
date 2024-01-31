#!/bin/sh

cd app
crond -b
python manage.py crontab add
python manage.py crontab show

exec "$@"
