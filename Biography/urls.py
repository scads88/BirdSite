# -*- coding: utf-8 -*-

from django.urls import path
from . import views


urlpatterns=[
        path("Biography/", views.index, name="index"),
        ]