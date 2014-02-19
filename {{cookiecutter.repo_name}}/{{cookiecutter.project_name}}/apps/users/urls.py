# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from apps.users import views

urlpatterns = patterns('',
    url(r'^$', views.UserListView.as_view(), name='list'),
    url(r'^(?P<username>[\w\-_]+)/$', views.UserDetailView.as_view(),
        name='detail'),
)
