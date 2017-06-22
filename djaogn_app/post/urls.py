from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_id>[0-9]+)/delete/$', views.post_delete, name='delete'),
    url(r'^(?P<post_id>[0-9]+)/modify/$', views.post_modify, name='modify'),
]