# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Disponibilities(models.Model):
    day = models.CharField(max_length=15, null=True, default=None)
    from_date = models.TimeField(verbose_name='From')
    to_date = models.TimeField(verbose_name='To')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'disponibility'
        verbose_name_plural = 'disponibilities'
        ordering = ['created_at']

    def __str__(self):
        return self.day
