# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from main.settings_deploy import DOMAIN_NAME
import main.settings_environ as settings_environ
if settings_environ.MAPBOX_KEY != None:
    # production settings; app is running on server
    from main.settings_environ import MAPBOX_KEY
else:
    # development settings; app is running locally
    from main.settings_sensitive import MAPBOX_KEY


from ..geography.views import Location
from ..business.models import BusinessManager
import models

from os import getcwd
import sqlite3
import datetime


def create(request):
    title = DOMAIN_NAME
    neighborhood = request.GET.get('neighborhood', 'Wicker Park').replace('+', ' ')

    # set default map
    location = Location(neighborhood).get_coordinates()

    jobs = Listings().retrieve_jobs()

    context = {
        'title': title,
        'location': location,
        'api_key': MAPBOX_KEY,
        'jobs': jobs
    }

    return render(request, "jobs/create.html", context)

def root(request):
    title = DOMAIN_NAME
    neighborhood = request.GET.get('neighborhood', 'Wicker Park').replace('+', ' ')

    if request.method == 'POST':
        #INSERT NEW JOB INTO DATABASE
        print('printing request.POST')
        #job = [posted_date, title, company, address, neighborhood, shift, description]
        job = models.Job(
            title = request.POST.get('title', ''),
            business = request.POST.get('company', ''),
            # TODO: Add to web form
            location = request.POST.get('location', ''),
            #TODO: Add to form
            job_function = request.POST.get('function', ''),
            #TODO: add to form
            employment_type = request.POST.get('employment_type', ''),
            description = request.POST.get('description', ''),
            #TODO: add to form
            skills = request.POST.get('skills', ''),
            #TODO: add to form
            qualifications = request.POST.get('qualifications', ''),
            #TODO: add to form
            instructions = request.POST.get('instructions', ''),
            #TODO: add to form
            poc = request.POST.get('poc', ''),
            email = request.POST.get('email', ''),
            phone = request.POST.get('phone', '')
            )
        job.save()

    # set default map
    location = Location(neighborhood).get_coordinates()

    # TODO: This should come from the Jobs model
    jobs = Listings().retrieve_jobs()

    context = {
        'title': title,
        'location': location,
        'api_key': MAPBOX_KEY,
        'jobs': jobs
    }

    return render(request, "jobs/index.html", context)


def update(request):
    pass


def get_one(request):
    pass


def get_all(request):
    pass


def get_area(request):
    pass


def insert_into_db(job):
    conn = sqlite3.connect(getcwd() + "/jobs.db")
    c = conn.cursor()
    c.execute("INSERT INTO 'Jobs' VALUES (?,?,?,?,?,?,?)", job)
    conn.commit()
    conn.close()

class Job(object):

    def __init__(self, job_data):
        self.title = job_data.get('title')
        self.posted_date = job_data.get('postedDate')
        self.company = job_data.get('company')
        # this will be a Location() object
        self.location = Location(job_data.get('location')).get_coordinates()
        self.shift = job_data.get('shift')
        self.description = job_data.get('description')
        self.tags = job_data.get('tags')


    def add_to_database(self):
        # TODO: move add_job() from db_script.py here
        pass



class Listings(list):

    def __init__(self, default_list=[]):
        super(Listings, self).__init__(default_list)
        self.db = getcwd() + "/jobs.db"
        self.raw_data = None

    def retrieve_jobs(self):
        return models.Job.objects.all()

    def convert_db_row_to_dict(self, db_data):
        dictionary = {
            'title': db_data[2],
            'postedDate': db_data[1],
            'company': db_data[3],
            'location': db_data[4],
            # Neighborhood (db_data[5]) is not used
            'shift': db_data[6],
            'description': db_data[7],
            'tags': ""
        }
        return dictionary

    def build_jobs(self):
        for row in self.raw_data:
            self.append(Job(self.convert_db_row_to_dict(row)))
        return self
