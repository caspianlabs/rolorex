#!/bin/bash

while ! nc -zv db.caspianlabs.org 5432; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up, starting Rolorex"
python manage.py migrate
gunicorn rolorex.wsgi:application -c python:rolorex.settings.gunicorn
