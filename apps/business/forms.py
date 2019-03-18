from django.forms import ModelForm, EmailInput, URLInput, TextInput
from django.utils.translation import ugettext_lazy as _
from datetime import date

from models import Business, Location
from ..app_form_templates import USPhoneNumberMultiWidget


def today_as_string():
    today = date.today().isoformat()
    return today

class NewBusiness(ModelForm):
    def __init__(self, data=None, *args, **kwargs):
        super(NewBusiness, self).__init__(data, *args, **kwargs)

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
            'email': EmailInput(attrs={'placeholder': _('email@domain.com')}),
            'website': URLInput(attrs={'placeholder': _('http://www.webaddress.com')}),
            'phone': USPhoneNumberMultiWidget(),
            'poc_role': TextInput(attrs={'placeholder': _('E.g., Manager, Human Resources Manager')})
        }


class NewLocation(ModelForm):
    def __init__(self, data=None, *args, **kwargs):
        super(NewLocation, self).__init__(data, *args, **kwargs)

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
