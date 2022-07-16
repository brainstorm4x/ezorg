from ast import Sub
from django.db import models

# Create your models here.
client_names =( 
    ('Labcorp', 'Labcorp'),
    ('Sevita', 'Sevita'),
    ('Cross Country', 'Cross Country'),
    ('Childrens', 'Childrens'),
    ('R1 RCM', 'R1 RCM'),
)

reminder_day = (
    ('Day 0', 'Day 0'),
    ('Day 1', 'Day 1'),
    ('Day 2', 'Day 2'),
    ('Day 3', 'Day 3'),
    ('Day 4', 'Day 4'),
    ('Day 5', 'Day 5'),
    ('Day 6', 'Day 6'),
)

class Subaccount(models.Model):
    subaccount_name = models.CharField(max_length=200)
    subaccount_id = models.IntegerField()

class Clients(models.Model):
    clientname = models.CharField(max_length=200, choices=client_names)

class ClientsInfo(models.Model):
    clientname = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    custid = models.IntegerField()
    subaccount = models.ForeignKey(Subaccount, null=True, on_delete=models.DO_NOTHING)
    client_mailbox = models.EmailField(unique=True)
    reminder_email_needed = models.BooleanField()
    first_reminder_day = models.CharField(choices=reminder_day, max_length=50, null=True, blank=True)
    second_reminder_day = models.CharField(choices=reminder_day, max_length=50, null=True, blank=True)
    third_reminder_day = models.CharField(choices=reminder_day, max_length=50, null=True, blank=True)
    
    