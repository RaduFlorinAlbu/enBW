from django.contrib import admin
from buckets.models import Bucket
from buckets.forms import BucketForm

class BucketAdmin(admin.ModelAdmin):
    form = BucketForm
# Register your models here.
admin.site.register(Bucket, BucketAdmin)