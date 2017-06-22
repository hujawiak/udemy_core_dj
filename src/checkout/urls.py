# coding=utf-8
from django.conf.urls import url, include
from . import views


app_name = 'checkout'
urlpatterns = [
    url(r'^$', views.checkout, name='checkout'),
]