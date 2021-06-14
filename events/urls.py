from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_event,name='add'),
    path('archive/',views.archive,name='archive'),
    path('', views.index, name='index'),
]

