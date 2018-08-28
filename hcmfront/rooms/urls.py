from django.conf.urls import url
from . import views

app_name = 'rooms'

urlpatterns = [
    url('', views.index, name='index'),
]
