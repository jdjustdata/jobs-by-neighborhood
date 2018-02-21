import os

from flask import Flask, render_template, request, redirect

from jbn.location import Location

app = Flask(__name__)
app.secret_key = "rendermaps"



@app.route("/")
def index():
    #set default map
    n = "Logan Square"
    if request.args.get('neighborhood'):
        n = request.args.get('neighborhood')
    return render_template("index.html", location=Location(n).build_url())


# default/404 redirect route
@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def not_found_route(path):
    return redirect('/')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
