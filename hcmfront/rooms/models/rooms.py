# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .supplies import Supplies


# Create your models here.
class Rooms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=70)
    capacity = models.IntegerField(default=1)
    supplies = models.ManyToManyField(Supplies, verbose_name='Supply', related_name='get_supplies')
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    status = models.ForeignKey(Supplies, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'
        ordering = ['created_at']

    def __str__(self):
        self.title
