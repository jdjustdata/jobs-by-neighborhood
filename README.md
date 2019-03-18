# jobs-by-neighborhood
Chi Hack Night Breakout Group. https://github.com/chihacknight/breakout-groups/issues/143
Search by role for entry-level jobs in your neighborhood

## Requirements
  * ~~Python 3~~ Python 2.7 (for now)
  * Python Packages: Django 1.11.5, requests
  * Python Django Packages in requirements.txt
  * To install Django requirements locally, use:
    pip install -r requirements.txt

  * Update March 2018 -- New pip requirement: django-localflavors --- used to collect geographic information (a managed list of states, urban centers, and zip codes)
    pip install django-localflavors
  * Update March 2018 -- New pip requirement: django-widget-tweaks --- used to help create customizeable and repeatable Bootstrap formatted forms with Django's form models
    pip install django-widget-tweaks
  * Update April 2018 -- Added pip requirements: mapbox and geojson
  * Update April 2018 -- Added pip requirements: django-crispy-forms and django-braces

    --- rerun "pip install -r requirements.txt" to install new packages

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

## translation

This project uses Django's internationalization i18n translation hooks. 

Reference Django's documentation for further details: https://docs.djangoproject.com/en/2.1/topics/i18n/translation/

TODO: Finish documentation

  * To evaluate all **.html**, **.txt**, and **.py** files for translatable text (identified by the *gettext* library method), 
  run this command: 
     
    ```django-admin makemessages -l es```
    
    ** If you are attempting to run this command on a mac, you may get a message informing you errors occurred while attempting to run msguniq. If you get this message, you must install gettext with Homebrew:
    
    ```brew install gettext```
    
    and then add the location where gettext installed to a PATH variable:
    
    ```PATH="/usr/local/opt/gettext/bin:$PATH"```
    
    Attempt to rereun the makemessages command. If you are still getting an error, you may need to run the getmessages command with python manage.py instead:
    
    ```python manage.py makemessages -l es```
  
  * This command will generate or update **.po** message files in the locale folder (*/main/locale/es*, where *es* 
  designates the language code).
  
  * Translators will update the **.po** files with relevant translations in the '*msgstr*' key.  
  
  * After you create and update **.po** files, run the following command to compile new messages for the gettext library:  
    
    ```django-admin compilemessages```
 