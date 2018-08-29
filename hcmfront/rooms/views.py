# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from .models import ReservRoom


class ReservListView(ListView):
    model = ReservRoom
