from django.db import models

# Create your models here.
class Event(models.Model):
    uuid = models.CharField(editable=False, max_length=30)
    title = models.CharField(max_length = 100, default=None, blank=True)
    message = models.TextField()