from secrets import choice
from django.db import models
from django.forms import ChoiceField

# Create your models here.
service_choice = (
    ("service1", "service1"),
    ("service2", "service2"),
    ("service3", "service3"),
    )

class Service(models.Model):
    service = models.CharField(choices=service_choice, max_length=225)