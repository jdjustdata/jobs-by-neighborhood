import csv
import sqlite3
from os import getcwd
from random import randint
from random import choice
import string

db_name = "jobs.db"
db_path = getcwd() + "/" + db_name

jobs_header = '''CREATE TABLE 'Jobs'
(PostedDate DATE, Title TEXT, Company TEXT, Address TEXT, Neighborhood TEXT, Shift TEXT, Description INT)'''

def create_table(query):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def add_job(location):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    rand_number = randint(0, 1000)
    title = "Job no." + str(rand_number)
    company = "Company no." + str(rand_number)
    address = location.json['features'][0]
    if address['properties']:
        print(address)
        address = address['properties']['address']
    else:
        address = address['place_name']
    print(address)
    neighborhood = location.json['features'][1]['context'][0]['text']
    print(neighborhood)
    shift = "shift " + str(randint(1, 4))
    description = ''.join(choice(
    string.ascii_letters + string.digits) for n in range(16))
    posted_date = "2018-03-06"
    job = [posted_date, title, company, address, neighborhood, shift, description]
    c.execute("INSERT INTO 'Jobs' VALUES (?,?,?,?,?,?,?)", job)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table(jobs_header)
