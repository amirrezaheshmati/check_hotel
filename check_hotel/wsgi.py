"""
WSGI config for check_hotel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import sys
import os

from django.core.wsgi import get_wsgi_application

path = "/home/amirrezaheshmati/check_hotel"
if path not in sys.path :
    sys.path.append(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'check_hotel.settings')

application = get_wsgi_application()