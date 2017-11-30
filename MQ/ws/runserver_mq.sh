#!/bin/sh
celery multi restart w1 -A ws -l info
python manage.py runserver 0.0.0.0:8000