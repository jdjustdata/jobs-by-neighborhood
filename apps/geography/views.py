# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

import requests
import main.settings_environ as settings_environ
if settings_environ.MAPBOX_KEY != None:
    # production settings; app is running on server
    from main.settings_environ import MAPBOX_KEY
else:
    # development settings; app is running locally
    from main.settings_sensitive import MAPBOX_KEY


# Construct and Use MapBox Location API
class Location(object):
    def __init__(self, neighborhood):
        self.url = None
        self.head = "https://api.mapbox.com/geocoding/v5/"
        self.map_type = "mapbox.places/"
        self.response_type = ".json"
        self.zoom = str(15)
        self.neighborhood = neighborhood

        # leading spaces to separate parameters
        self.city = " Chicago"
        self.state = " IL"
        self.coordinates = None
        self.json = None


    def build_url(self):
        print MAPBOX_KEY
        self.url = self.head + self.map_type + self.neighborhood + self.city + \
                   self.state + self.response_type + "?access_token=" + MAPBOX_KEY
        self.url = self.url.replace(" ", "+").replace(",", "%2C")
        print self.url
        return self


    def retrieve_json(self):
        r = requests.get(self.url)
        return r.json()


    def get_coordinates(self):
        self.build_url()
        j = self.retrieve_json()
        self.json = j

        # reverse coordinates order
        latitude = j['features'][0]['center'][1]
        longitude = j['features'][0]['center'][0]
        self.coordinates = [latitude, longitude]
        return self
