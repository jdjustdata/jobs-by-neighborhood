import os

api_key = None
with open(os.getcwd()+"/keys.txt", "r") as key_doc:
    api_key = key_doc.read()

class Location(object):

    def __init__(self, neighborhood):
        self.url = None
        self.head =  "https://maps.googleapis.com/maps/api/staticmap"
        self.zoom = str(15)
        self.size = "500x400"
        self.neighborhood = neighborhood
        self.city = "Chicago"
        self.state = "IL"


    def build_url(self):
        self.url = self.head + "?" + "center=" + self.neighborhood + ","+ self.city + "," + self.state + "&zoom=" + self.zoom + "&size=" + self.size + "&key=" + api_key

        self.url.replace(" ", "+").replace(",", "%2C")
        return self
