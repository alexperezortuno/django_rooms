from django.conf.urls import url
from .views import ReservListView, ReservCreateView

app_name = 'rooms'

rooms_patterns = ([
    url(r'^$', ReservListView.as_view(), name='reserve_list'),
    url(r'^create/$', ReservCreateView.as_view(), name='reserve_create'),
], 'rooms')
