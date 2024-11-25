
from django.db import models
class Bank(models.Model):
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    ifsc=models.CharField(max_length=50)
    noOfCustomers=models.IntegerField()
    turnOver=models.IntegerField()
    def __str__(self):
        return self.name
