# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .supplies import Supplies
from .status import Status
from .rooms import Rooms
from .disponibilities import Disponibilities


class ReservRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True)
    additional_supplies = models.ManyToManyField(Supplies,
                                                 verbose_name='Additional Supply',
                                                 related_name='get_addtional_supplies')
    capacity = models.IntegerField(default=1)
    hours = models.ManyToManyField(Disponibilities, verbose_name='Hours reserved', related_name='get_reserv_hours')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'reserv'
        verbose_name_plural = 'reservs'
        ordering = ['created_at']

    def __str__(self):
        return self.room.title
