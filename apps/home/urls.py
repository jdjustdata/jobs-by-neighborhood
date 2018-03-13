from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^search/', views.index, name="search_loc"),
    url(r'^test', views.test, name="test_map"),

    url(r'^', views.index, name="home"),
]
