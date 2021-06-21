import django_filters
from django_filters import DateFilter
from django.forms import DateField, widgets
from .models import Event

class EventFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='start_date',lookup_expr="gte")
    end_date = DateFilter(field_name='end_date',lookup_expr="lte")
    class Meta:
        model = Event
        fields = ['category','start_date','end_date']
 
