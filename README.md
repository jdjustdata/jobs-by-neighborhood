# jobs-by-neighborhood
Search by role for entry-level jobs in your neighborhood

## Requirements
  * Python 3
  * Python Packages: flask, requests

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





## resources

  * our github - https://github.com/chihacknight/breakout-groups/issues/143

  * Chicago Health Atlas (potential overlay data) - https://chicagohealthatlas.org/resources
  * Chicago Health Atlas API - https://chicagohealth.herokuapp.com/apidoc

  * GeoJson (test coordinates) -  http://geojson.io/#map=8/44.418/-88.064

### mapping tools
Need to use a "Slippy" map

  * Google Maps - https://developers.google.com/maps/documentation/javascript/

  * Mapbox - https://www.mapbox.com/api-documentation/#introduction
