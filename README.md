# jobs-by-neighborhood
Chi Hack Night Breakout Group. https://github.com/chihacknight/breakout-groups/issues/143
Search by role for entry-level jobs in your neighborhood

## Requirements
  * Python 3
  * Python Packages: flask, requests
  * Python Django Packages in requirements.txt
  * To install Django requirements locally, use:
    pip install -r requirements.txt

## Use Cases
  - Users:
    1. Job Seeker
    2. Job Poster
    3. Admin (Chamber of Commerce or similar)

  - Job Seeker
    * Use map to find open position in my neighborhood.
    * Search by role for open positions in Chicago (maybe list of places sorted
      by distance from home)

  - Job Poster
    * submit a job posting w/ location, title, description, contact info
    * remove a job posting that has been filled

  - Admin
    * confirm a job submission and have it appear on site
    * remove job posting that has expired
    * notify Job Poster of expired job posting

## Objects, Methods, and Attributes
  * Map (JavaScript)
  * Display page
    - Map
    - List of Jobs
    - Search bar (location, roles)
  * Job
    - Title (role)
    - Company
    - Location
      * neighborhood (Lakeview, Ravenswood, etc.)
      * street address
      * Coordinates (for map rendering)
    - Shift
    - Tags
    - Description
    - Posted Date / Submission Date
  * Job List
    - filterBy / sortBy
      * expiration
      * location
      * Role


## IDEAS

How to get data on places that have openings and filter out similar places that
do not

Web scraping service that constantly updates common locations
    List of cleaning services, plumbers, etc.
    Use our list to connect with Places API data to render the locations we need



## GETTING STARTED IN DEVELOPMENT

This section applies to the project conversion to Django.
To setup this project locally, you must complete a couple small steps.
Django is managed by a set of settings files. To keep this project
secure and ready to run in multiple environments, there are a couple
settings files located in the main directory:
  * settings.py -- global settings
  * settings_developer.py -- sets up the development environment
    ** Not pushed to the Git Repository
    ** You will need to remove the .template file extension when you first clone the directory, and edit this file for your local environment
  * settings_deploy.py -- sets up the deployed/production environment
  * settings_sensitive.py -- stores sensitive keys
    ** NOT pushed to the Git Repository for security reasons
    ** You will need to remove the .template file extension when you
    first clone the directory, and edit this file for your local environment and protected keys.
    ** NOTE: If you add sensitive keys to the project, please update the template file and inform the developer community so they can add their own keys to their local development environment
  * settings_environ.py -- retrieves environmental variables set on the   server for the production environment
    ** This is pushed to the Git Repository, and should not store sensitive information

Run the server locally from the project root directory with:
  python manage.py runserver

## GETTING STARTED IN DEPLOYMENT

This section applies to the project conversion to Django.
To deploy this project to a production server, keep in mind the following:
  * Django selects the appropriate settings from the variable DJANGO_SETTINGS_MODULE
    - This is set by default in manage.py to settings_developer.py
    - The default setting applies a development environment
    - To override the default on a production environment, simply set an environmental variable on the server to:
      "DJANGO_SETTINGS_MODULE": "main.settings_deploy"
  * Set environmental variables on the server to store other sensitive keys and information with the appropriate key names matching settings_envrion.py

## resources

  * our github - https://github.com/chihacknight/breakout-groups/issues/143

  * Chicago Health Atlas (potential overlay data) - https://chicagohealthatlas.org/resources
  * Chicago Health Atlas API - https://chicagohealth.herokuapp.com/apidoc

  * GeoJson (test coordinates) -  http://geojson.io/#map=8/44.418/-88.064

### mapping tools

  * Mapbox - https://www.mapbox.com/api-documentation/#introduction

  * Leafletjs - http://leafletjs.com/examples/quick-start/

  * Google Maps - https://developers.google.com/maps/documentation/javascript/
