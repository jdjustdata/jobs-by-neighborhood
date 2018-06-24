# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

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
from ..jobs.models import Job


def index(request):
    title = DOMAIN_NAME
    neighborhood = request.GET.get('neighborhood', 'Wicker Park').replace('+', ' ')

    # set default map
    location = Location(neighborhood).get_coordinates()

    # jobs = Listings().retrieve_jobs().build_jobs()
    jobs = Job.objects.all()

    context = {
        'title': title,
        'location': location,
        'api_key': MAPBOX_KEY,
        'jobs': jobs
    }
    return render(request, "home/index.html", context)


def search(request):
    # retrieve query from the request
    query = request.GET.get('neighborhood', 'Wicker Park').replace('+', ' ')
    # process query and get relevant map data
    location = Location(query).get_coordinates()
    # return map data and update page
    return HttpResponse(str(location.coordinates))
    #return HttpResponse("This is the Search route")


def test(request):
    context = {
        'access_token': MAPBOX_KEY
    }
    return render(request, "home/test_map.html", context)


def eggs(request):
    return "Poop"
