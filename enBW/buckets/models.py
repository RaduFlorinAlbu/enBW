from django.db import models
from events.models import Event
# Create your models here.
class Bucket(models.Model):
    name = models.CharField(max_length = 100, default=None, blank=True)
    events = models.ForeignKey(Event, on_delete=models.CASCADE)