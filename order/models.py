from typing_extensions import Required
from django.db import models

from candidate.models import Candidate
from service import Service
from client import Clients

# Create your models here.
class Orders(models.Model):
    candidateinfo = models.ForeignKey(Candidate, on_delete=models.DO_NOTHING)
    serviceinfo = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    orderid = models.IntegerField(null=True, blank=True)
    requestid = models.IntegerField(null=True, blank=True)
    urgent = models.BooleanField(default=False)