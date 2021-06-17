from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_event,name='add'),
    path('archive/',views.archive,name='archive'),
    path('event/<int:pk>/', views.event_detail,name="event_detail"),
    path('', views.index, name='index'),
    path('event/<int:pk>/delete',views.delete_event,name='delete_event'),
]

