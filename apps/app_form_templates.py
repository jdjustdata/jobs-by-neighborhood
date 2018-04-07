from django import forms
from django.core.validators import RegexValidator

import re


class USPhoneNumberMultiWidget(forms.MultiWidget):
    """
    A Widget that splits US Phone number input into three <input type='text'> boxes.
    """

    def __init__(self, attrs={}):
        widgets = (
            forms.TextInput(
                attrs={
                    'size': '3',
                    'maxlength': '3',
                    'class': 'phone text-center',
                    'required': False,
                }),
            forms.TextInput(
                attrs={
                    'size': '3',
                    'maxlength': '3',
                    'class': 'phone text-center',
                    'required': False,
                }),
            forms.TextInput(
                attrs={
                    'size': '4',
                    'maxlength': '4',
                    'class': 'phone text-center',
                    'required': False,
                }),
            forms.TextInput(
                attrs={
                    'size': '8',
                    'maxlength': '8',
                    'class': 'phone text-left',
                    'required': False,
                }),
        )
        super(USPhoneNumberMultiWidget, self).__init__(widgets)


    def decompress(self, value):
        if value:
            return re.split('-| ext.', value)
        return (None, None, None, None)

    def value_from_datadict(self, data, files, name):
        value = [u'', u'', u'', u'']
        # look for keys like name_1, get the index from the end
        # and make a new list for the string replacement values
        for d in filter(lambda x: x.startswith(name), data):
            index = int(d[len(name) + 1:])
            value[index] = data[d]
        if value[0] == value[1] == value[2] == value[3] == u'':
            return None
        if value[3] == u'':
            # print u'{}-{}-{}'.format(value[0], value[1], value[2])
            return u'{}-{}-{}'.format(value[0], value[1], value[2])
        else:
            # print u'{}-{}-{} ext.{}'.format(value[0], value[1], value[2], value[3])
            return u'{}-{}-{} ext.{}'.format(value[0], value[1], value[2],
                                         value[3])


class PhoneField(forms.MultiValueField):
    widget = USPhoneNumberMultiWidget

    def __init__(self, *args, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter an area code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            forms.CharField(
                required=False,
                error_messages={'incomplete': 'Enter an area code.'},
                validators=[
                    RegexValidator(r'^[0-9]{3}$', 'Enter a valid area code.'),
                ],
            ),
            forms.CharField(
                required=False,
                error_messages={'incomplete': 'Enter a phone number.'},
                validators=[
                    RegexValidator(r'^[0-9]{3}$',
                                   'Enter a valid phone number.')
                ],
            ),
            forms.CharField(
                required=False,
                validators=[
                    RegexValidator(r'^[0-9]{4}$',
                                   'Enter a valid phone number.')
                ],
            ),
            forms.CharField(
                required=False,
                validators=[
                    RegexValidator(r'^[0-9]{0,8}$', 'Enter a valid extension.')
                ],
                label="Extension"
            ),
        )
        super(PhoneField, self).__init__(
            error_messages=error_messages,
            fields=fields,
            required=False,
            require_all_fields=False,
            *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return '-'.join(data_list)
        return None
