from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^create/', views.create, name="create"),
    url(r'^(?P<id>[0-9]+)', views.get_one, name="get_one"),
    url(r'^all', views.get_all, name="get_all"),
    url('', views.root, name="root")

]
