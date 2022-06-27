from django.db import models

# Create your models here.
vendor_choice =(
    ("eScreen", "eScreen"),
    ("LabCorp", "LabCorp"),
    ("Quest", "Quest"),
)

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200, choices=vendor_choice)
    has_integration = models.BooleanField()