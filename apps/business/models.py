# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator, EmailValidator, URLValidator
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

# Imported filter was created to sort database queries ignoring letter case
from ..app_filters import case_insensitive_criteria
from industries import INDUSTRY_INDEX

# Import Localflavor for US Geographic data
# Reference documentation: http://django-localflavor.readthedocs.io/en/latest
from localflavor.us.us_states import US_STATES
from localflavor.us.models import USZipCodeField

from main.settings import BASE_DIR
import os
import json


INDUSTRY_KEY_FIELD = 'industries'
INDUSTRY_CODE = 'industry_code'
INDUSTRY_NAME = 'industry_title'
SUBINDUSTRIES = 'sub_industries'
JSON_FILE = os.path.join(BASE_DIR, 'static', 'base', 'json', 'naics_industries.json')
INDUSTRY_INDEX_FILE = os.path.join(BASE_DIR, 'apps', 'business', 'industries.py')

PHONE_REGEX = RegexValidator(
    regex=r'^\d{3}-\d{3}-\d{4}(\sext.\d{1,5})?$',
    message=_("Phone number must be entered in the format: '999-999-9999'."))

STATUS_CODES = [
    ('submitted', _('Submitted')),
    ('review', _('Under Review')),
    ('approved', _('Approved'))
]

# TODO: Simplify the industry list -- perhaps, adopt a list of categories used by Google Places
def get_industry_choices(key_field=INDUSTRY_KEY_FIELD):
    # Return a tuple of field choices from a json file of industry categories
    # Import NAICS Industry categories from US Bureau of Labor Statistics JSON data
    with open(JSON_FILE) as f:
        json_data = json.load(f)
        choices_list = []
        if key_field in json_data:
            industries = json_data[key_field]
            for industry in industries:
                choices_list.append((industry[INDUSTRY_CODE], industry[INDUSTRY_NAME][0]))
    choices_list = sort_list(choices_list)
    return tuple(choices_list)


def index_industries():
    # Generate an index of the industries in the JSON file
    # Index key = Industry Code; value = Industry Name
    index = {}
    with open(JSON_FILE) as f:
        json_data = json.load(f)
        if INDUSTRY_KEY_FIELD in json_data:
            industries = json_data[INDUSTRY_KEY_FIELD]
            for industry in industries:
                index[industry[INDUSTRY_CODE]] = industry[INDUSTRY_NAME][0]
                if SUBINDUSTRIES in industry:
                    for sub in industry[SUBINDUSTRIES]:
                        index[sub[INDUSTRY_CODE]] = sub[INDUSTRY_NAME]
    with open(INDUSTRY_INDEX_FILE, 'w') as fw:
        fw.write('INDUSTRY_INDEX = {}'.format(index))
    return


def get_industry_subchoices(parent_industry_code):
    # Return a tuple of field choices from a json file of industry categories
    # Import NAICS Industry categories from US Bureau of Labor Statistics JSON data
    with open(JSON_FILE) as f:
        json_data = json.load(f)
        choices_list = []

        industries = json_data[INDUSTRY_KEY_FIELD]
        for industry in industries:
            if industry[INDUSTRY_CODE] == parent_industry_code:
                for sub in industry[SUBINDUSTRIES]:
                    choices_list.append((sub[INDUSTRY_CODE],
                                        sub[INDUSTRY_NAME]))
                break
    choices_list = sort_list(choices_list)
    return tuple(choices_list)


def sort_list(choices):
    return sorted(choices, key=lambda choice: choice[1])



class BusinessManager(models.Manager):

    def get_all(self, sort_field=None, default="name"):
        if sort_field == None:
            sort_field = default
        if "created_at" in sort_field or "updated_at" in sort_field:
            lower_field = sort_field
            order_field = sort_field
        else:
            lower_field, order_field = case_insensitive_criteria(sort_field)
        businesses = (Business.objects.all()
                    .extra(select={'lower_field':lower_field})
                    .order_by(order_field))
        for b in businesses:
            b.industry = INDUSTRY_INDEX[b.industry]
        return businesses

    def get_total(self):
        # totals = {}
        pass
        # totals['total'] = Contact.objects.all().count()
        # return totals

    def get_or_create_contact(self, first_name, last_name, email):
        # created = False
        pass
        # try:
        #     contact = Contact.objects.get(email=email)
        # except Contact.DoesNotExist:
        #     contact = Contact.objects.create(
        #         first_name=first_name,
        #         last_name=last_name,
        #         email=email
        #     )
        #     created = True
        # return contact, created

    def update_timestamp(self, email):
        pass
        # contact = Contact.objects.get(email=email)
        # contact.save()
        # return


class Business(models.Model):
    name = models.CharField(
        verbose_name=_("Business"),
        help_text=_("Name of your business"),
        max_length=100
    )
    industry = models.CharField(
        verbose_name=_("Industry Category"),
        help_text=_("What is the primary industry for your business?"),
        max_length=2,
        default="",
        choices=get_industry_choices(),
        validators=[
            RegexValidator(
                regex='^[0-9]{2}$',
                message=_('Please select an industry from the list.')
            )
        ]
    )
    subindustry = models.CharField(
        verbose_name=_("Industry Type"),
        max_length=3,
        default="",
        blank=True,
        choices=get_industry_subchoices('72')
    )
    website = models.CharField(
        verbose_name=_("Website"),
        help_text=_("Businesses with website and contact information are more likely to get interested applicants."),
        max_length=100,
        blank=True,
        validators=[URLValidator()]
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=100,
        blank=True,
        validators=[EmailValidator()]
    )
    phone = models.CharField(
        verbose_name=_("Phone"),
        max_length=20,
        blank=True,
        validators=[PHONE_REGEX]
    )
    primary_poc = models.CharField(
        verbose_name=_("Primary Contact"),
        help_text=_("Who is the primary person that should be contacted for job verification?"),
        max_length=50,
        blank=True
    )
    poc_role = models.CharField(
        verbose_name=_("Role (Contact)"),
        help_text=_("What is this person's role?"),
        max_length=30,
        blank=True
    )
    created_by = models.ForeignKey(
        User,
        verbose_name=_("Created by"),
        on_delete=models.PROTECT,
        related_name="businesses_created"
    )
    created_at = models.DateTimeField(
        verbose_name=_("Date Created"),
        auto_now_add=True
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=10,
        default=STATUS_CODES[0],
        choices=STATUS_CODES
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Date Updated"),
        auto_now=True
    )
    objects = BusinessManager()



class LocationManager(models.Manager):
    pass


class Location(models.Model):
    name = models.CharField(
        verbose_name=_("Location"),
        help_text=_("If your business has multiple locations, please name this location."),
        max_length=50,
        default=_("Primary")
    )
    business = models.ForeignKey(
        Business,
        verbose_name=_("Business"),
        on_delete=models.CASCADE,
        related_name="locations"
    )
    is_primary = models.BooleanField(
        verbose_name=_("Primary Location"),
        help_text=_("Is this the primary (default) location for your business?"),
        default=True
    )
    street = models.CharField(
        verbose_name=_("Street Address"),
        max_length=50,
        default="",
        blank=True,
        null=True
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=50,
        default=""
    )
    state = models.CharField(
        verbose_name=_("State"),
        max_length=2,
        default="IL",
        choices=US_STATES
    )
    zipcode = USZipCodeField(
        verbose_name=_("Zip Code"),
        blank=True
    )
    longitude = models.DecimalField(
        verbose_name=_("Longitude"),
        max_digits=12,
        decimal_places=8,
        default=0
    )
    latitude = models.DecimalField(
        verbose_name=_("Latitude"),
        max_digits=12,
        decimal_places=8,
        default=0
    )
    neighborhood = models.CharField(
        verbose_name=_("Neighborhood"),
        max_length=50,
        blank=True,
        default=''
    )
    phone = models.CharField(
        verbose_name=_("Phone"),
        help_text=_("Does this location have a unique phone number?"),
        max_length=20,
        blank=True,
        validators=[PHONE_REGEX]
    )
    #objects = LocationManager()
