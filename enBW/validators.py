from django.core.validators import RegexValidator

"""
This file has been created to group all validators, not add them in forms
Useful for further development of the project
"""

bucket_name_validator = RegexValidator( 
    r'^[\w-]+$',
    message="This field must only contain letters, numbers, hyphens, and underscores."
)