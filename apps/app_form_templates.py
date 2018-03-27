from django import forms
from django.core.validators import RegexValidator


class USPhoneNumberMultiWidget(forms.MultiWidget):
    """
    A Widget that splits US Phone number input into three <input type='text'> boxes.
    """

    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(
                attrs={
                    'size': '3',
                    'maxlength': '3',
                    'class': 'phone',
                    'required': False,
                }),
            forms.TextInput(
                attrs={
                    'size': '3',
                    'maxlength': '3',
                    'class': 'phone',
                    'required': False,
                }),
            forms.TextInput(
                attrs={
                    'size': '4',
                    'maxlength': '4',
                    'class': 'phone',
                    'required': False,
                }),
            forms.TextInput(
                attrs={
                    'size': '5',
                    'maxlength': '5',
                    'class': 'phone',
                    'required': False,
                }),
        )
        super(USPhoneNumberMultiWidget, self).__init__(widgets, attrs)


    def decompress(self, value):
        if value:
            return value.split('-')
        return (None, None, None)

    def value_from_datadict(self, data, files, name):
        value = [u'', u'', u'']
        # look for keys like name_1, get the index from the end
        # and make a new list for the string replacement values
        for d in filter(lambda x: x.startswith(name), data):
            index = int(d[len(name) + 1:])
            value[index] = data[d]
        if value[0] == value[1] == value[2] == u'':
            return None
        return u'%s-%s-%s' % tuple(value)


class PhoneField(forms.MultiValueField):
    widget = USPhoneNumberMultiWidget

    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter an area code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            forms.CharField(
                error_messages={'incomplete': 'Enter an area code.'},
                validators=[
                    RegexValidator(r'^[0-9]{3}$', 'Enter a valid area code.'),
                ],
                required=False,
            ),
            forms.CharField(
                error_messages={'incomplete': 'Enter a phone number.'},
                validators=[
                    RegexValidator(r'^[0-9]{3}$',
                                   'Enter a valid phone number.')
                ],
                required=False,
            ),
            forms.CharField(
                validators=[
                    RegexValidator(r'^[0-9]{4}$',
                                   'Enter a valid phone number.')
                ],
                required=False,
            ),
            forms.CharField(
                validators=[
                    RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')
                ],
                required=False,
                label="Extension"
            ),
        )
        super(PhoneField, self).__init__(
            error_messages=error_messages,
            fields=fields,
            required=False,
            require_all_fields=False)


        def compress(self, data_list):
            return '-'.join(data_list)
