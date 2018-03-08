import os

from flask import Flask, render_template, request, redirect

from jbn.location import Location
from db_script import add_job
import api_keys

app = Flask(__name__)
app.secret_key = "rendermaps"

api_key = api_keys.mapbox_key


@app.route("/")
def index():
    # set default map
    n = "Logan Square"
    if request.args.get('neighborhood'):
        n = request.args.get('neighborhood')
    location = Location(n).get_coordinates()
    # add_job(location)
    return render_template("index.html", location=location, api_key=api_key)


# default/404 redirect route
@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def not_found_route(path):
    return redirect('/')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
