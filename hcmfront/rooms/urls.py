from django.conf.urls import url
from .views import ReservListView

app_name = 'rooms'

urlpatterns = [
    url(r'^$', ReservListView.as_view(), name='reserv-list'),
]
