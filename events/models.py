from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Event(models.Model):
    image = models.ImageField(upload_to='upload/',null=True,blank=True,default='images/blank.jpg')
    organizer = models.CharField(max_length=50)
    title = models.CharField(max_length=80)
    description = RichTextField(blank=False)
    start_time = models.TimeField(auto_now=False,auto_now_add=False,default = timezone.now)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False,auto_now_add=False)
    location = models.CharField(max_length=100)
    price = models.IntegerField(blank=True,null=True,default = 0)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
