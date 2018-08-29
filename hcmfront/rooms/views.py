# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from .models import ReservRoom
from .forms import ReservRoomForm


class ReservListView(ListView):
    model = ReservRoom


@method_decorator(staff_member_required, name='dispatch')
class ReservCreateView(CreateView):
    template_name = 'rooms/reservroom_form.html'
    model = ReservRoom
    form_class = ReservRoomForm
    success_url = reverse_lazy('rooms:reserv_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReservCreateView, self).form_valid(form)
