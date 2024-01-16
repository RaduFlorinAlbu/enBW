from django.contrib import admin
from buckets.models import Bucket
from buckets.forms import BucketForm

class BucketAdmin(admin.ModelAdmin):
    form = BucketForm
    list_display = ["name"]
# Register your models here.
admin.site.register(Bucket, BucketAdmin)