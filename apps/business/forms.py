from django.forms import ModelForm, EmailInput, URLInput, TextInput
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import date, datetime

from models import Business, Location
from ..app_form_templates import USPhoneNumberMultiWidget, PhoneField


def today_as_string():
    today = date.today().isoformat()
    return today

class NewBusiness(ModelForm):
    def __init__(self, data=None, *args, **kwargs):
        super(NewBusiness, self).__init__(data, *args, **kwargs)

        self.fields['name'].help_text = "Name of your business"
        self.fields['industry'].help_text = "What is the primary industry for your business?"
        self.fields['website'].help_text = "Businesses with website and contact information are more likely to get interested applicants."

        self.fields['primary_poc'].label = "Primary Contact"
        self.fields['poc_role'].label = "Role (Contact)"
        self.fields['primary_poc'].help_text = "Who is the primary person that should be contacted for job verification?"
        self.fields['poc_role'].help_text = "What is this person's role?"

    class Meta:
        model = Business
        fields = [
            'name',
            'industry',
            'subindustry',
            'website',
            'email',
            'phone',
            'primary_poc',
            'poc_role'
        ]
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'email@domain.com'}),
            'website': URLInput(attrs={'placeholder': 'http://www.webaddress.com'}),
            'phone': USPhoneNumberMultiWidget(),
            'poc_role': TextInput(attrs={'placeholder': 'E.g., Manager, Human Resources Manager'})
        }


class NewLocation(ModelForm):
    def __init__(self, data=None, *args, **kwargs):
        super(NewLocation, self).__init__(data, *args, **kwargs)

        self.fields['name'].help_text = "If your business has multiple locations, please name this location."
        self.fields['is_primary'].label = "Primary Location"
        self.fields['is_primary'].help_text = "Is this the primary (default) location for your business?"
        self.fields['phone'].help_text = "Does this location have a unique phone number?"

    class Meta:
        model = Location
        fields = [
            'name',
            'is_primary',
            'street',
            'city',
            'state',
            'zipcode',
            'phone'
        ]
        widgets = {
            'phone': USPhoneNumberMultiWidget()
        }
