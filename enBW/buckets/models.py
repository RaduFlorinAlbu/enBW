from django.db import models
from validators import bucket_name_validator
# Create your models here.
class Bucket(models.Model):
    name = models.CharField(max_length = 100, default=None, blank=False, validators=[bucket_name_validator])
    