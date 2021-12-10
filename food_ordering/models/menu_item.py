
from django.db import models

from . import Category
from .audit import UserAudit
from django.utils.translation import ugettext_lazy as _
from food_ordering.models.restaurant import Restaurant


class MenuItem(UserAudit):
    """
        it can be defined permission to user for adding menu items for now whole user can add.
    """
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, verbose_name=_('categories'), blank=True,)
    restaurant = models.ForeignKey(Restaurant, models.CASCADE)

    class Meta:
        verbose_name = _("Menu Item")
        verbose_name_plural = _("Menu Items")
        db_table = "menu_item"

    def __str__(self):
        return self.name

