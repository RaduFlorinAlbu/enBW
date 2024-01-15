import json
import re

from django import forms
from utils import get_setting
from buckets.models import Bucket

class BucketForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        valid_bucket_name = get_setting("EXAMPLE_VALID_BUCKET_NAME")
        info_text = (f"Use only letters, numbers, hyphens or underscores , e.g. {valid_bucket_name}")
        """
        Here it is added only indication on how a bucket should be name
        The actual validation will be done in models
        This is because, if done here, it will apply only to admin interface
        """
        try:
            self.fields["name"].help_text = info_text
            self.fields["name"].widget.attrs["placeholder"] = valid_bucket_name
        except KeyError:
            pass    