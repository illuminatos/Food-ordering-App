
from django.db import models
from .audit import UserAudit
from django.utils.translation import ugettext_lazy as _


class Category(UserAudit):
    """
        it can be defined permission to user for adding category for now whole user can add.
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = "category"

    def __str__(self):
        return self.name
