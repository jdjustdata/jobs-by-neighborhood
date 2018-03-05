import os
import api_keys
import requests
import json


api_key = api_keys.mapbox_key


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

    def build_url(self):
        self.url = self.head + self.map_type + self.neighborhood + self.city + \
                   self.state + self.response_type + "?access_token=" + api_key

        self.url.replace(" ", "+").replace(",", "%2C")
        return self

    def retrieve_json(self):
        r = requests.get(self.url)
        return r.json()

    def get_coordinates(self):
        self.build_url()
        j = self.retrieve_json()
        # reverse coordinates order
        latitude = j['features'][0]['center'][1]
        longitude = j['features'][0]['center'][0]
        self.coordinates = [latitude, longitude]
        return self

