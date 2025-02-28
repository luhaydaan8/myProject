
"""
WSGI config for farm_tools project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
setting_module = farm_tools.deployment if  "RENDER_EXTERNAL_HOSTNAME" in os.environ else "farm_tools.settings"
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_tools.settings')

application = get_wsgi_application()