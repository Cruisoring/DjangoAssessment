from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField

from .models import Car


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


class BuyForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('Status',)
        widgets = {}

    def clean_date(self):
        buyer = self.cleaned_data.get("BuyerName")
        mobile = self.cleaned_data.get('BuyerMobile')
        if buyer == '':
            raise ValidationError("Buyer name is mandatory")
        if mobile == '':
            raise ValidationError("Buyer mobile is mandatory")
        return self.cleaned_data


class ConfirmForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConfirmForm, self).__init__(*args, **kwargs)
        # self.commission = CharField(label='The Dodgy Brothers commission (5%) in dollars:',
        #                    initial=f'{self.cleaned_data["AskingPrice"]*0.05}')
        # self.net = CharField(label='The net amount that is transferrable to the seller:',
        #                    initial=f'{self.cleaned_data["AskingPrice"]*0.95}')
        instance = getattr(self, 'instance', None)
        price = int(instance.AskingPrice)
        self.fields['commission'] = CharField(label='The Dodgy Brothers commission (5%) in dollars:', 
            initial=f'{price*0.05}')

        self.fields['net_amount'] = CharField(label='The Dodgy Brothers commission (5%) in dollars:', 
            initial=f'{price*0.95}')

        instance.Status = 'Sold'

        for field in self.fields:
            try:
                field.widget.attrs['readonly'] = True
            except:
                pass

    # def clean_sku(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         return instance.sku
    #     else:
    #         return self.cleaned_data['sku']

    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('Status',)
        widgets = {}