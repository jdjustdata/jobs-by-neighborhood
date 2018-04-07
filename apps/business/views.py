# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

import json, geojson
import main.settings_environ as settings_environ
if settings_environ.MAPBOX_KEY != None:
    from main.settings_environ import MAPBOX_KEY
else:
    from main.settings_sensitive import MAPBOX_KEY
from mapbox import Geocoder

from forms import NewBusiness, NewLocation
from models import Business, BusinessManager, Location, get_industry_choices, get_industry_subchoices, index_industries


def create_form(request):
    form = NewBusiness()        # New business form template
    index_industries()          # Refresh the industry index from the industry JSON
    choices = get_industry_choices()
    sub_choices = get_industry_subchoices('92')

    context = {
        'form': form,
        'choices': choices,
        'sub_choices': sub_choices
    }
    return render(request, 'business/create.html', context)


def create_submit(request):
    if request.method == 'POST':
        # use forms.py to validate form data
        form = NewBusiness(request.POST)
        if form.is_valid():
            # form data is valid
            business = form.save()      # Create business object
            return redirect(reverse('business:add_location', kwargs={'id':business.id}))
        else:
            # form data has validation errors
            request.session['form_errors'] = form.errors
    return redirect(reverse('business:add'))


def add_location_form(request, id):
    business = get_object_or_404(Business, id=id)
    form = NewLocation()

    context = {
        'business': business,
        'form': form,
    }
    return render(request, 'business/location_add.html', context)

def add_location_submit(request, id):
    if request.method == 'POST':
        # use forms.py to validate form data
        form = NewLocation(request.POST)
        if form.is_valid():
            # form data is valid
            business = get_object_or_404(Business, id=id)       # Get business object

            geocoder = Geocoder(access_token=MAPBOX_KEY)        # Gather geocode data
            response = geocoder.forward(
                address=form.cleaned_data['street'] \
                    + " " + form.cleaned_data['city'] \
                    + " " + form.cleaned_data['state'] \
                    + " " + form.cleaned_data['zipcode'],
                limit=1
            )
            features = response.geojson()['features'][0]

            Location.objects.create(
                name=form.cleaned_data['name'],
                business=business,
                is_primary=form.cleaned_data['is_primary'],
                street=form.cleaned_data['street'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                zipcode=form.cleaned_data['zipcode'],
                longitude=features["geometry"]["coordinates"][0],
                latitude=features["geometry"]["coordinates"][1],
                neighborhood=features["context"][0]["text"],
                phone=form.cleaned_data['phone']
            )
            return redirect(reverse('business:get_all'))
        else:
            # form data has validation errors
            print "ERRORS"
            request.session['form_errors'] = form.errors
    return redirect(reverse('business:add_location', kwargs={'id': id}))


def update_location_form(request, biz_id, loc_id):
    business = get_object_or_404(Business, id=biz_id)
    location = get_object_or_404(Location, id=loc_id)
    form = NewLocation(instance=location)
    locations = Location.objects.exclude(id=location.id).filter(business=biz_id)

    context = {
        'business': business,
        'location': location,
        'locations': locations,
        'form': form,
        'api_key': MAPBOX_KEY
    }
    return render(request, 'business/location_update.html', context)


def update_location_submit(request, biz_id, loc_id):
    if request.method == 'POST':
        # use forms.py to validate form data
        form = NewLocation(request.POST)
        if form.is_valid():
            # form data is valid
            business = get_object_or_404(Business, id=biz_id)   # Get business object

            geocoder = Geocoder(access_token=MAPBOX_KEY)        # Gather geocode data
            response = geocoder.forward(
                address=form.cleaned_data['street'] \
                    + " " + form.cleaned_data['city'] \
                    + " " + form.cleaned_data['state'] \
                    + " " + form.cleaned_data['zipcode'],
                limit=1
            )
            features = response.geojson()['features'][0]

            location = get_object_or_404(Location, id=loc_id)   # Get location object to update
            location.name = form.cleaned_data['name']           # Update attributes with form data
            location.business = business
            location.is_primary = form.cleaned_data['is_primary']
            location.street = form.cleaned_data['street']
            location.city = form.cleaned_data['city']
            location.state = form.cleaned_data['state']
            location.zipcode = form.cleaned_data['zipcode']
            location.longitude = features["geometry"]["coordinates"][0]
            location.latitude = features["geometry"]["coordinates"][1]
            location.neighborhood = features["context"][0]["text"]
            location.phone = form.cleaned_data['phone']

            location.save()
            return redirect(reverse('business:get_all'))
        else:
            # form data has validation errors
            print "ERRORS"
            request.session['form_errors'] = form.errors
    return redirect(reverse('business:add_location', kwargs={'id': id}))


def get_one(request):
    pass


def get_all(request, sort_field=None):
    businesses = Business.objects.get_all(sort_field)
    context = {
        'businesses': businesses
    }
    return render(request, 'business/all_list.html', context)


def get_area(request):
    pass