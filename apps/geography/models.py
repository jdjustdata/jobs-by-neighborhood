# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Imported filter was created to sort database queries ignoring letter case
from ..app_filters import case_insensitive_criteria

# Import Localflavor for US Geographic data
# Reference documentation: http://django-localflavor.readthedocs.io/en/latest
from localflavor.us.us_states import US_STATES
from localflavor.us.models import USZipCodeField

# class Neighborhood(models.Model):
#     name = models.CharField(max_length=50)
#     slug = models.CharField(max_lengh=50)
#     geo_type = models.CharField(max_length=50)
#     geometry = models.CharField(max_length=2000)
#     centroid = models.CharField(max_length=255, default='')
#     part = models.CharField(max_length=50, default='')
#     resource_cnt = models.IntegerField(default=0)

