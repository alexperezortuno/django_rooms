# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Supplies(models.Model):
    title = models.CharField(max_length=70)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'supply'
        verbose_name_plural = 'supplies'
        ordering = ['created_at']

    def __str__(self):
        return self.title
