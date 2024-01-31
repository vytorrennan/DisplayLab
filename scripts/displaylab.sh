#!/usr/bin/env bash

scripts/wait-for-it.sh pgdb:5432 -t 30
cd app
python manage.py migrate --no-input
python createSuperUser.py
gunicorn DisplayLab.wsgi:application --bind 0.0.0.0:8000
