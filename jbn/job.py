
from jbn.location import Location

class Job(object):

    def __init__(self, job_data):
        self.title = job_data.get('title')
        self.posted_date = job_data.get('postedDate')
        self.company = job_data.get('company')
        # this will be a Location() object
        self.location = job_data.get('location')
        self.shift = job_data.get('shift')
        self.description = job_data.get('description')
        self.tags = job_data.get('tags')

    def add_to_database(self):
        # TODO: move code from db_script.py here
        pass
        
