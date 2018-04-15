# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse

import main.settings_environ as settings_environ
from main.settings_deploy import DOMAIN_NAME
if settings_environ.MAPBOX_KEY != None:
    # production settings; app is running on server
    from main.settings_environ import MAPBOX_KEY
else:
    # development settings; app is running locally
    from main.settings_sensitive import MAPBOX_KEY


from ..geography.views import Location
from ..jobs.views import Listings


def index(request):
    title = DOMAIN_NAME
    neighborhood = request.GET.get('neighborhood', 'Wicker Park').replace('+', ' ')

    # set default map
    location = Location(neighborhood).get_coordinates()

    # jobs = Listings().retrieve_jobs().build_jobs()
    jobs = []

    context = {
        'title': title,
        'location': location,
        'api_key': MAPBOX_KEY,
        'jobs': jobs
    }
    return render(request, "home/index.html", context)

def test(request):
    context = {
        'access_token': MAPBOX_KEY
    }
    return render(request, "home/test_map.html", context)
