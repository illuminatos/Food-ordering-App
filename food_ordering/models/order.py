from django.db import models
from django.contrib.postgres.fields import JSONField
from .audit import UserAudit
from django.utils.translation import ugettext_lazy as _

from datetime import datetime, timedelta


class OrderModel(UserAudit):
    STATUS_APPROVED = 'Approved'
    STATUS_WAITING = 'Waiting'

    STATUS = (
        (STATUS_APPROVED, _('Approved')),
        (STATUS_WAITING, _('Waiting')),
    )
    menu_items = models.JSONField(default=dict)
    user = models.CharField(max_length=200, blank=True, editable=False, null=True)
    status = models.CharField(_('Status'), max_length=20, choices=STATUS, default=STATUS_WAITING)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        db_table = "order"


