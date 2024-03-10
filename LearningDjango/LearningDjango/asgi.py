"""
ASGI config for project LearningDjango.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# asgi/wsgi 文件用于接收网络请求wsgi同步方式，asgi异步方式，大多数还是用wsgi

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearningDjango.settings')

application = get_asgi_application()
