# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Status(models.Model):
    title = models.CharField(max_length=70)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'status'
        ordering = ['created_at']

    def __str__(self):
        self.title
