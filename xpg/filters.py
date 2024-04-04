import django_filters
from .models import ecmodel

class ecFilter(django_filters.FilterSet):

    class Meta:
        model = ecmodel
        fields = ['name', 'category','price']