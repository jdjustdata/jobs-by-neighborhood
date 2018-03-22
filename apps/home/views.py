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

# MT Code to be moved elsewhere
from ..jobs.views import Job
from os import getcwd
import sqlite3
db_path = getcwd() + "/jobs.db"

def retrieve_jobs(db):
    query = """SELECT * FROM Jobs"""
    conn = sqlite3.connect(db)
    c = conn.cursor()
    print(db_path)
    retrieved = c.execute(query).fetchall()
    for r in retrieved:
        print(r)
    conn.commit()
    conn.close()
    return retrieved

def convert_db_row_to_dict(db_data):
    dictionary = {
        'title': db_data[1],
        'postedDate': db_data[0],
        'company': db_data[2],
        'location': db_data[3],
        # Neighborhood (db_data[4]) is not used
        'shift': db_data[5],
        'description': db_data[6],
        'tags': ""
    }
    return dictionary


def build_jobs(db_rows):
    jobs_list = []
    for row in db_rows:
        jobs_list.append(Job(convert_db_row_to_dict(row)))
    return jobs_list



def index(request):
    title = DOMAIN_NAME
    neighborhood = request.GET.get('neighborhood', 'Wicker Park').replace('+', ' ')

    # set default map
    location = Location(neighborhood).get_coordinates()

    # add_job(location)
    # Mike T
    db_data = retrieve_jobs(db_path)
    jobs = build_jobs(db_data)
    for j in jobs:
        print(j.location.coordinates)

    context = {
        'title': title,
        'location': location,
        'api_key': MAPBOX_KEY,
        # MT Code
        'jobs': jobs
    }
    return render(request, "home/index.html", context)

def test(request):
    context = {
        'access_token': MAPBOX_KEY
    }
    return render(request, "home/test_map.html", context)
