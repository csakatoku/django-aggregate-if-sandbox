# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.db.models import Q

from aggregate_if import Count, Sum, Max

from maxif.offers.models import Offer


class Command(BaseCommand):
    def handle(self, **options):
        res = Offer.objects.annotate(
            max_price=Max('price'),
            max_price_open=Max('price', only=Q(status=Offer.OPEN)),
        )

        print(res.query)
        print(res)
