#!/bin/sh

echo "Waiting for django..."

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000

echo "Django started"


exec "$@"