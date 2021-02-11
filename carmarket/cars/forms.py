from datetime import date

from django.forms import Form, ModelForm, DateInput, TimeInput, TextInput, IntegerField, TypedChoiceField
from django.core.exceptions import ValidationError

from .models import Car, Make, Years


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {}

    def clean_date(self):
        d = self.cleaned_data.get("Year")
        if d > date.today().year:
            raise ValidationError("Year cannot be future")
        return d

class FilterForm(Form):
    make = TypedChoiceField(required=False)
    year = TypedChoiceField(required=False)

    # class Meta:
    #     model = Car
    #     fields = ['make', 'year']
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(FilterForm, self).__init__(*args, **kwargs)