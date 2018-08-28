# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=70)
    capacity = models.IntegerField(default=1)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
