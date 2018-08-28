# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from .supplies import Supplies
from .disponibilities import Disponibilities


class Rooms(models.Model):
    title = models.CharField(max_length=70)
    max_capacity = models.IntegerField(default=1)
    supplies = models.ManyToManyField(Supplies, verbose_name='Supply', related_name='get_supplies')
    disponiblity = models.ManyToManyField(Disponibilities,
                                          verbose_name='Disponibility',
                                          related_name='get_disponibilities')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def dates_available(self):
        try:
            return ", ".join(['{day} - {f}:{t}'.format(day=f.day,
                                                       f=f.from_date.strftime('%H:%M'),
                                                       t=f.to_date.strftime('%H:%M')) for f in self.disponiblity.all()])
        except Exception as err:
            print(err)
            return None

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'
        ordering = ['created_at']

    def __str__(self):
        return self.title
