# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator, URLValidator
from main.settings_environ import DOMAIN_NAME
from datetime import date, datetime, timedelta

# Imported filter was created to sort database queries ignoring letter case
from ..app_filters import case_insensitive_criteria

# Import Localflavor for US Geographic data
# Reference documentation: http://django-localflavor.readthedocs.io/en/latest
from localflavor.us.us_states import US_STATES
from localflavor.us.models import USZipCodeField

import re
import os


class BusinessManager(models.Manager):
    def get_all(self, sort_field="none", default="first_name"):
        model_field_name = sort_field_translator(sort_field, default)
        if "created_at" in model_field_name or "updated_at" in model_field_name:
            lower_field = model_field_name
            order_field = model_field_name
        else:
            lower_field, order_field = case_insensitive_criteria(
                model_field_name
            )
        contacts = (Contact.objects.all()
                    .extra(select={'lower_field':lower_field})
                    .order_by(order_field))
        return contacts

    def get_total(self):
        totals = {}
        totals['total'] = Contact.objects.all().count()
        return totals

    def get_or_create_contact(self, first_name, last_name, email):
        created = False
        try:
            contact = Contact.objects.get(email=email)
        except Contact.DoesNotExist:
            contact = Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            created = True
        return contact, created
    def update_timestamp(self, email):
        contact = Contact.objects.get(email=email)
        contact.save()
        return


class Business(models.Model):        
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(
        max_length=2, 
        default="IL",
        choices=US_STATES
    )
    zipcode = USZipCodeField()
    website = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        validators=[URLValidator()]
    )
    email = models.EmailField(
        max_length=100, 
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BusinessManager()

