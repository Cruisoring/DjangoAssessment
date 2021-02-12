import django_filters

from cars.models import Car


class CarFilter(django_filters.FilterSet):

    class Meta:
        model = Car
        fields = {
            'Make',
            'Year',
        }
