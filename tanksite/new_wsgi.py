# -- coding: utf-8 --
import os
import sys
import platform
#путь к проекту, там где manage.py
sys.path.insert(0, '/home/vadimmonroe/django_site_prj')
#путь к фреймворку, там где settings.py
sys.path.insert(0, '/home/vadimmonroe/django_site_prj/tanksite')
#путь к виртуальному окружению myenv
sys.path.insert(0, '/home/vadimmonroe/django_site_prj/venv/bin/python3.10')

os.environ["DJANGO_SETTINGS_MODULE"] = "tanksite.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

