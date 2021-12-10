from django.db import models


class DateTimeStamping(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add updates on creation only
    updated_at = models.DateTimeField(auto_now=True)  # auto_now updates field each time

    class Meta:
        abstract = True  # Abstract base class for some common info


class UserAudit(DateTimeStamping):
    created_by = models.CharField(max_length=100, blank=True, editable=False, null=True) # todo güncelleme var mı burda
    updated_by = models.CharField(max_length=255, blank=True, editable=False, null=True)

    class Meta:
        abstract = True  # Abstract base class for some common info

# todo it can be written get_username method with using tls on middlewares to save user name or id
