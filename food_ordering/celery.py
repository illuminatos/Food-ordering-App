import os

from celery import Celery
from food_ordering import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')

app = Celery('food_ordering')

app.config_from_object('food_ordering:settings')

app.autodiscover_tasks(settings.INSTALLED_APPS)



