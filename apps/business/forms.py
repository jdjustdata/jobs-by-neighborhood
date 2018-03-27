from django.forms import ModelForm, EmailInput, URLInput
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import date, datetime

from models import Business
from ..app_form_templates import USPhoneNumberMultiWidget, PhoneField


def today_as_string():
    today = date.today().isoformat()
    return today

class NewBusiness(ModelForm):
    def __init__(self):
        super(NewBusiness, self).__init__()
        self.fields['phone'] = PhoneField()

        self.fields['name'].help_text = "Name of your business"
        self.fields['industry'].help_text = "What is the primary industry for your business?"
        self.fields['website'].help_text = "Businesses with website and contact information are more likely to get interested applicants."

    class Meta:
        model = Business
        fields = [
            'name',
            'industry',
            'subindustry',
            'street',
            'city',
            'state',
            'zipcode',
            'website',
            'email',
            'phone'
        ]
        widgets = {
            'email': EmailInput,
            'website': URLInput,
            'phone': USPhoneNumberMultiWidget()
        }

