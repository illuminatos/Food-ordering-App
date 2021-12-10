
from django.db import models
from .audit import UserAudit
from django.utils.translation import ugettext_lazy as _


class Restaurant(UserAudit):
    """
    it can be defined permission to user for adding restaurant for now whole user can add restaurant.
    """
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurants")
        db_table = "restaurant"

    def __str__(self):
        return self.name

