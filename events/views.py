from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
from django.urls import reverse
# Create your views here.
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Wydarzenie zostało dodane pomyślnie!")
            return redirect(reverse('add'))
        else:
            messages.error(request,"Ups coś poszło nie tak spróbuj jeszcze raz...")
            return redirect(reverse('add'))

        # return HttpResponseRedirect(reverse('index'))
    else:
        form = EventForm()
    return render(request,"events/form.html",{"form":form})


def index(request):
    events = Event.objects.all()
    return render(request,'events/index.html',{'events': events})
