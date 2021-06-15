import django_filters

from django_filters import  CharFilter

from .models import Salat




class Salatfilter(django_filters.FilterSet):
    #names = CharFilter(field_name = 'names', lookup_expr = 'icontains')
    class Meta:
        model = Salat
       

        fields = {
            'names':['icontains'],
            
            'week':['iexact']  
        }