import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogsite.settings")
django.setup()