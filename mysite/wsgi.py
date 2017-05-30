"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import os
import sys
import django
'''
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = get_wsgi_application()
'''
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

path =
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#'/Users/froyvalencia/Desktop/newsRank/mysite'
sys.path.append(os.path.join(BASE_DIR, 'newsRank', 'mysite')
#if path not in sys.path:
#    sys.path.append(path)
django.setup()
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
