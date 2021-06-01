from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('id','image','organizer','title','description','start_date',
                  'end_date','location','price','published')
