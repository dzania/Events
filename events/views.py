from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from .models import Event
from .filters import EventFilter
from django.urls import reverse
from django.utils import timezone

# main page view to show only upcoming events
def index(request):
    now = timezone.now()
    events = Event.objects.filter(start_date__gt=now).order_by('start_date')
    
    myFilter = EventFilter(request.GET,queryset=events)
    events = myFilter.qs

    return render(request,'events/index.html',{'events': events, "myFilter": myFilter})

#view for adding events form
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Wydarzenie zostało dodane pomyślnie!")
            return redirect(reverse('add'))
        else:
            messages.error(request,"Ups coś poszło nie tak spróbuj jeszcze raz...")
            return redirect(reverse('add'))
    else:
        form = EventForm()
    return render(request,"events/form.html",{"form":form})

# view for sorting passed events
def archive(request):
    now = timezone.now()
    passed_events = Event.objects.filter(start_date__lt=now).order_by('-start_date')

    myFilter = EventFilter(request.GET, queryset=passed_events)
    passed_events = myFilter.qs

    return render(request,"events/archive.html",{'passed_events':passed_events,"myFilter":myFilter})

#detail event view
def event_detail(request,pk):
    event = get_object_or_404(Event,pk=pk)
    return render(request, 'events/event_detail.html',{'event':event})


def delete_event(request,pk):
    event = get_object_or_404(Event,pk=pk)
    event.delete()
    return redirect('index')
