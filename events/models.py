from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField()
    published = models.DateTimeField(default=timezone.now)
