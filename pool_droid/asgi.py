"""
ASGI config for pool_droid project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from asgi_middleware_static_file import ASGIMiddlewareStaticFile
from django.conf import settings
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pool_droid.settings')

application = get_asgi_application()
application = ASGIMiddlewareStaticFile(
  application, static_url=settings.STATIC_URL,
  static_root_paths=[settings.STATIC_ROOT]
)
