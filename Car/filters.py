import django_filters
from .models import Car
class CarFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Car
        fields = ['carMake']