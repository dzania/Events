from django.forms import ModelForm, DateField, widgets
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['published']
        labels = {
            'image':'Zdjęcie',
            'organizer':'Organizator',
            'title':'Nazwa',
            'description':'Opis',
            'start_time':'Godzina rozpoczęcia',
            'start_date':'Data rozpoczęcia',
            'end_date':'Data zakończenia',
            'location':'Miejsce',
            'price':'Cena',
        }
        widgets = {
            'start_time': widgets.TimeInput(attrs={'type':'time'},format='%H:%M'),
            'start_date': widgets.DateInput(attrs={'type': 'date'}),
            'end_date': widgets.DateInput(attrs={'type': 'date'})
        }
