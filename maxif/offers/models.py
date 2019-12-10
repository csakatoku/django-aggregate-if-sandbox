from __future__ import unicode_literals

from django.db import models


class Offer(models.Model):
    user_id = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(max_length=30)
    expire_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    OPEN = "OPEN"
    REVOKED = "REVOKED"
    PAID = "PAID"
