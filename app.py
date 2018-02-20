import os

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "rendermaps"

api_key = None
with open(os.getcwd()+"/keys.txt", "r") as key_doc:
    api_key = key_doc.read()

class Location(object):

    def __init__(self, neighborhood, city):
        self.url = None
        self.head =  "https://maps.googleapis.com/maps/api/staticmap"
        self.zoom = "13"
        self.size = "500x400"
        self.neighborhood = neighborhood
        self.city = city
        self.state = "IL"

    def build_url(self):
        self.url = self.head + "?" + "center=" + self.neighborhood + ","+ self.city + "," + self.state + "&zoom=" + self.zoom + "&size=" + self.size + "&key=" + api_key

        self.url.replace(" ", "+").replace(",", "%2C")
        return self

@app.route("/")
def index():
    return render_template("index.html", location=Location("Logan Square", "Chicago").build_url())


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
