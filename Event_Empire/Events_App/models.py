from django.db import models

# Create your models here.

class Event_Info(models.Model):
    
    Party_Name = models.CharField(max_length=300)
    Location = models.CharField(max_length=300)
    Age_Criteria = models.IntegerField()
    Amount = models.IntegerField()
    Event_Details = models.CharField(max_length=1600)
    Venue = models.CharField(max_length=300)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Party_Starting_Date = models.CharField(max_length=100)
    Image = models.CharField(max_length=1000)
    
    