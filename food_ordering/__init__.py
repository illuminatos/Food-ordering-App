
from .celery import app as celery_app


default_app_config = 'food_ordering.apps.Config'

__all__ = ['celery_app']