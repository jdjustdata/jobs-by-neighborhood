from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^add/', views.create_form, name="add"),
    url(r'^create/', views.create_submit, name="create"),
    url(r'^(?P<id>[0-9]+)/location/add', views.add_location_form, name="add_location"),
    url(r'^(?P<id>[0-9]+)/location/create', views.add_location_submit, name="create_location"),
    url(r'^(?P<biz_id>[0-9]+)/location/(?P<loc_id>[0-9]+)/edit', views.update_location_form, name="edit_location"),
    url(r'^(?P<biz_id>[0-9]+)/location/(?P<loc_id>[0-9]+)/update', views.update_location_submit, name="update_location"),
    url(r'^(?P<id>[0-9]+)', views.get_one, name="get_one"),
    url(r'^all', views.get_all, name="get_all"),
    url(r'^all/(?P<sort_field>[-a-z_]+)', views.get_all, name="get_all"),
]
