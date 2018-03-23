# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from ..geography.views import Location
from os import getcwd
import sqlite3


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
        query = """SELECT * FROM Jobs"""
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        self.raw_data = retrieved = c.execute(query).fetchall()
        conn.commit()
        conn.close()
        return self

    def convert_db_row_to_dict(self, db_data):
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

    def build_jobs(self):
        for row in self.raw_data:
            self.append(Job(self.convert_db_row_to_dict(row)))
        return self
