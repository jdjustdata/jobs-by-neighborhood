# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse

import main.settings_environ as settings_environ
if settings_environ.MAPBOX_KEY != None:
    # production settings; app is running on server
    from main.settings_environ import MAPBOX_KEY
else:
    # development settings; app is running locally
    from main.settings_sensitive import MAPBOX_KEY


from ..geography.views import Location

def index(request, neighborhood="Logan Square"):
    title = "Jobs By Neighborhood"

    # set default map
    # if request.args.get('neighborhood'):
    #     n = request.args.get('neighborhood')
    location = Location(neighborhood).get_coordinates()

    # add_job(location)

    context = {
        'title': title,
        'location': location,
        'api_key': MAPBOX_KEY
    }
    return render(request, "home/index.html", context)
