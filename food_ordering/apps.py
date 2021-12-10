from django.apps import AppConfig
import logging
logger = logging.getLogger(__name__)


class Config(AppConfig):
    name = 'food_ordering'
    label = 'food_ordering'

    def ready(self):
        logger.debug("Importing food_ordering related services...")
        try:
            from . import models
            from .tasks import publish_message

        except ImportError as ie:
            logger.exception(ie)
        except Exception as e:
            logger.exception(e)
        logger.debug("Done!")


