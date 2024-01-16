from django.db import models
from buckets.models import Bucket
import uuid

# Create your models here.
class Event(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)
    title = models.CharField(max_length = 100, default=None, blank=False)
    message = models.TextField()
    bucket = models.ForeignKey(Bucket, related_name='bucket', on_delete=models.CASCADE, null=True, blank=True)