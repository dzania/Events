from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .forms import EventForm
from .models import Event
# Create your views here.
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Event created successfully")
        return HttpResponseRedirect('events/index.html')
    else:
        form = EventForm()
    return render(request,"events/form.html",{"form":form})


def index(request):
    all_objects = Event.objects.all()
    return render(request,'events/index.html',{'all_objects': all_objects})
