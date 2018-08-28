# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib import admin
from .models import (
                    Rooms,
                    Supplies,
                    Status,
                    ReservRoom,
                    Disponibilities)


class DisponibilitiesAdmin(admin.ModelAdmin):
    list_display = ('day', 'from_date', 'to_date')
    readonly_fields = ('created_at', 'updated_at')


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'dates_available')
    readonly_fields = ('created_at', 'updated_at')


class ReservRoomForm(forms.ModelForm):
    def save(self, commit=True):
        form_instance = super(ReservRoomForm, self).save(commit=False)
        # TODO: fix that
        try:
            form_instance.user = self.user

            if commit:
                form_instance.save()
        except Exception as e:
            print(e)

        return form_instance


class ReservRoomAdmin(admin.ModelAdmin):
    list_display = ('user', 'room')
    readonly_fields = ('created_at', 'updated_at')
    form = ReservRoomForm

    def get_form(self, request, *args, **kwargs):
        self.exclude = []

        if not request.user.is_superuser:
            self.exclude.append('user')

        form_instance = super(ReservRoomAdmin, self).get_form(request, *args, **kwargs)

        try:
            if not request.user.is_superuser:
                form_instance.user = request.user
        except Exception as e:
            print(e)

        return form_instance


admin.site.register(Status)
admin.site.register(Supplies)
admin.site.register(Disponibilities, DisponibilitiesAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(ReservRoom, ReservRoomAdmin)
