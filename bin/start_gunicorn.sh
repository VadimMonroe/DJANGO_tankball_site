#!/bin/bash
source /home/vadimmonroe/django_site_prj/venv/bin/activate

#exec gunicorn wsgi --pythonpath=/home/vadimmonroe/django_site_prj/venv/bin/python3.10 --bind 127.0.0.1:8001
#environment=PYTHONPATH="/home/vadimmonroe/django_site_prj/venv/bin/python3.10"
exec gunicorn -c "/home/vadimmonroe/django_site_prj/tanksite/gunicorn_config.py" tanksite.wsgi



