import os

from django.core.wsgi import get_wsgi_application

# change the config.development to your required setting module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

application = get_wsgi_application()
