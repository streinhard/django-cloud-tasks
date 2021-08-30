"""
WSGI config for sample project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import time

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapp.settings')

tic = time.perf_counter()
application = get_wsgi_application()
toc = time.perf_counter()
print(f"Django startup time: {toc - tic:0.4f}s")