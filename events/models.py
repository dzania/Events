from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    image = models.ImageField(upload_to='upload',null=True,blank=True)
    organizer = models.CharField(max_length=50)
    title = models.CharField(max_length=80)
    description = models.TextField()
    start_time = models.TimeField(auto_now=False,auto_now_add=False,default = timezone.now)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=True)
    location = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
